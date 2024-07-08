import mysql.connector
from mysql.connector import Error
import pandas as pd

# Replace these with your MySQL credentials
host = 'localhost'
database = 'jobs'
user = 'root'
password = 'root@392000'

# Establish a connection to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    if connection.is_connected():
        print('Connected to MySQL database')
        
        # Define the query
        query = "SELECT * FROM vacancy;"
        
        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query)
        
        # Fetch all the rows and column names
        rows = cursor.fetchall()
        column_names = cursor.column_names
        
        # Convert to DataFrame
        df = rows
        
        print(type(rows))

except Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    # Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed.')


from pinecone.grpc import PineconeGRPC as Pinecone

# If interacting with Pinecone via HTTP requests, use:
# from pinecone import Pinecone

pc = Pinecone(api_key="f606009e-5b47-4dae-88e8-d5c494deddd5")
index = pc.Index("db")

index.upsert(df)
