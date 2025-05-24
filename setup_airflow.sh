#!/bin/bash
# Set AIRFLOW_HOME to a specific folder in the current directory
export AIRFLOW_HOME=$(pwd)/airflow_home
echo "AIRFLOW_HOME set to $AIRFLOW_HOME"

# Add to shell configuration for persistence
echo "export AIRFLOW_HOME=$(pwd)/airflow_home" >> ~/.zshrc
source ~/.zshrc

# Activate virtual environment
source airflow_env/bin/activate

# Install Airflow 2.0.1 with constraints
uv add apache-airflow==2.10.5 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.12.txt"

# Initialize Airflow database
airflow db migrate

# Create admin user
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

echo "Airflow setup complete. Start services with:"
echo "airflow api-server -p 3000"
echo "airflow scheduler"