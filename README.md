# job_assignment
Data Pipeline with Airflow and PostgreSQL
Overview

This project showcases a data pipeline that generates sample data and loads it into a PostgreSQL database, orchestrated using Apache Airflow and containerized with Docker.

## Directory Hierarchy
```
|—— airflow
|    |—— dags
|        |—— data_loading.py
|        |—— loading_dag.py
|        |—— sample_data.py
|    |—— logs
|    |—— plugins
|    |—— script
|        |—— entry-point.sh
|—— docker-compose.yml
|—— Dockerfile
|—— docker_pgadmin_servers.json
|—— postgres
|    |—— docker_postgres_init.sql
|—— READMEs.md
|—— requirements.txt
```
- docker-compose.yml: Contains Docker Compose configuration.
- dags/: Directory for Airflow DAG definitions.
- data_sample/: Location for generated sample data.
- plugins/ (if applicable): Directory for custom Airflow plugins.
- requirements.txt: Lists Python dependencies.
- Additional Information

## Prerequisites:
- `Docker`
- `Docker compose`

## Installation

### Clone the project repository:

Bash
- `git clone https://github.com/Pattarapon2706/job_assignment.git`

### Navigate to the project directory:

Bash
- `cd job_assignment`

### Start the Docker containers:

Bash
- Build docker
```
docker-build
```
- Deploy images to container
```
`docker-compose up`
```

## Usage

- Access the Airflow web UI at http://localhost:8080
- Log in with the default credentials (username: `airflow`, password: `airflow`).
### Trigger the DAG:
- Locate the DAG named `data_loading_dag` in the Airflow UI.
- Toggle the DAG to ON to enable it.
- Click the "Trigger DAG" button to initiate the pipeline.

## Testing

Monitor the DAG's progress in the Airflow UI.
Verify data generation in the data_sample folder.
Confirm data loading into the PostgreSQL database.




Database Design Diagram: Refer to the database_design.png file.
