# Use the official Apache Airflow image as the base image
FROM apache/airflow:2.8.0

USER root

# Install development tools and PostgreSQL development headers
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

USER airflow

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run airflow db init, create connections, and create an admin user
# CMD ["bash", "-c", "airflow db init && airflow connections create-default-connections && airflow users create --role Admin --username admin --password admin --email admin@example.com --firstname foo --lastname bar"]
