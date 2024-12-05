# Steps to Reproduce Airflow Setup in a Python Virtual Environment

## Prerequisites
- Python version: 3.8.20
- Recommended version management: pyenv or asdf(prederred)

## Setup Instructions

### 1. Set Up Python Environment
```bash
python -m venv /<path>/.venv
source <path>/.venv/bin/activate
```

### 2. Install Airflow
```bash
pip install "apache-airflow[celery]==2.10.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.8.txt"
```

### 3. Create .env File
```bash
AIRFLOW_HOME=<custom_path>
```

### 4. Initialize Airflow
```bash
airflow db init
airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin
//create password
airflow standalone
```

### 5. Access Airflow Web Interface
- Navigate to `localhost:8080`
- Login with the created user credentials

**Note:** Optionally configure a custom DAGs folder in the `airflow.cfg` file.