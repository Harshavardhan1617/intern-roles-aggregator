# Steps to Reproduce Airflow Setup in a Python Virtual Environment

This guide explains how to set up Apache Airflow in a Python virtual environment using Python 3.8.20. Follow these steps to get started.

---

## Prerequisites
1. **Python 3.8.20**: Ensure Python 3.8.20 is installed. Use **asdf** (preferred) or **pyenv** to set up the local Python version.
2. **Virtual Environment**: Familiarity with creating and using Python virtual environments.

---

## Setup Instructions

### Step 0: Configure Python Version
Set your Python version to **3.8.20**:
- Using `asdf`:
  ```bash
  asdf install python 3.8.20
  asdf local python 3.8.20


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