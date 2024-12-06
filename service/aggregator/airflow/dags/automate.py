from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import json
import sys
import tempfile
import os

sys.path.append('/home/harsha/code/side_projects/tech_news_aggregator/service/aggregator')
from loader import MongoLoader
from mongoDBcollections import internship_collection
from links import internshala_url
from scrapers.internshala_scraper import scraper

default_args = {
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='internshala_etl',
    default_args=default_args,
    description='ETL workflow for Internshala scraper',
    schedule='0 9,21 * * *',  
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    @task
    def extract():
        url = internshala_url
        response = requests.get(url)
        response.raise_for_status()
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_extract:
            temp_extract.write(response.text)
            extract_path = temp_extract.name
        
        print(f"Extracted HTML content and saved to {extract_path}")
        return extract_path

    @task
    def transform(extract_path: str):
        with open(extract_path, "r") as f:
            soup = BeautifulSoup(f.read(), "lxml")
        
        dataObject = scraper(soup)
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_transform:
            json.dump(dataObject, temp_transform)
            transform_path = temp_transform.name
        
        # Clean up extract file
        os.unlink(extract_path)
        
        print(f"Transformed data and saved to {transform_path}")
        return transform_path

    @task
    def load(transform_path: str):
        with open(transform_path, "r") as f:
            dataObject = json.load(f)
        
        MongoLoader(dataObject=dataObject, collection=internship_collection)
        
        # Clean up transform file
        os.unlink(transform_path)
        
        print("Loaded data into MongoDB")

    extract_task = extract()
    transform_task = transform(extract_task)
    load_task = load(transform_task)