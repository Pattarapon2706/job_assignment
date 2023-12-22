import psycopg2
import pandas as pd
import pathlib

# Connect to your database (replace placeholders with your credentials)
conn = psycopg2.connect(
    host="postgres",
    database="demo1",
    user="postgres",
    password="password"
)

# Create a cursor object
cur = conn.cursor()

# Function to load Parquet data and insert into tables
def load_parquet_data(parquet_path):
    df = pd.read_parquet(parquet_path)
    # Handle Department table (no changes needed)
    unique_departments = df['department_name'].unique()
    for department_name in unique_departments:
        cur.execute("SELECT EXISTS (SELECT 1 FROM Department WHERE department_name = %s)", (department_name,))
        department_exists = cur.fetchone()[0]
        if not department_exists:
            cur.execute("INSERT INTO Department (department_name) VALUES (%s)", (department_name,))

    # Handle Sensor table (no changes needed)
    unique_sensors = df['sensor_serial'].unique()
    for sensor_serial in unique_sensors:
        df_sensor = df[df['sensor_serial'] == sensor_serial]
        department_name = df_sensor['department_name'].iloc[0]  # Assuming consistent department_name for each sensor
        cur.execute("SELECT EXISTS (SELECT 1 FROM Sensor WHERE sensor_serial = %s)", (sensor_serial,))
        sensor_exists = cur.fetchone()[0]

        if not sensor_exists:
            cur.execute("INSERT INTO Sensor (sensor_serial, department_name) VALUES (%s, %s)",
                    (sensor_serial, department_name))
        
    product_ids = []

    # Handle Product table (using surrogate key, removing department_name)
    for index, row in df.iterrows():
        cur.execute("INSERT INTO Product (product_name, sensor_serial, create_at) VALUES (%s, %s, %s) RETURNING product_id",
                (row['product_name'], row['sensor_serial'], row['create_at']))
        product_id = cur.fetchone()[0]  # Fetch the generated product_id for this specific row
        product_ids.append(product_id)

    # Handle ProductExpiry table (referencing product_id)
    for index, row in df.iterrows():
        product_id = product_ids[index]  # Example using a list
        cur.execute(
                "INSERT INTO ProductExpiry (product_id, expiry_date, create_at) VALUES (%s, %s, %s)",
                (product_id, row['product_expire'], row['create_at'])
        )

# Iterate through Parquet files in a folder (replace with your folder path)
for parquet_file in pathlib.Path("data_sample").glob("*.parquet"):
    load_parquet_data(parquet_file)

# Commit changes to the database
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()
