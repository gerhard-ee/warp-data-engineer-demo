#!/usr/bin/env python3
"""
WARP AI COMMAND DEMONSTRATION SCRIPT

This file provides a demonstration outline for creating a Snowflake data upload script
using Warp's AI Command features. Instead of containing the actual script, this file
shows how a Data Engineer would use Warp's AI Commands to generate the script during
a live demo.

INSTRUCTIONS FOR VIDEO DEMONSTRATION:
Follow the commented sections below, using each as a prompt for Warp's AI Command 
feature during your video.
"""

# DEMO SECTION 1: Script Setup
# In your Warp terminal, use AI Command (Ctrl+`) and type:
# "Create a Python script that imports the necessary libraries for connecting to Snowflake and manipulating data"
# 
# Expected AI Command output would generate:
# ------------------------------------
# import os
# import pandas as pd
# import numpy as np
# from datetime import datetime
# import snowflake.connector
# import logging
# from dotenv import load_dotenv
# 
# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
# 
# # Load environment variables from .env file
# load_dotenv()
# ------------------------------------
# 
# VIDEO NARRATION: "Notice how Warp's AI Command instantly generates the correct imports
# and sets up logging. I can quickly add this to my script without having to remember
# all the necessary imports."


# DEMO SECTION 2: Snowflake Connection Function
# In Warp, use AI Command and type:
# "Write a Python function to connect to Snowflake using environment variables"
# 
# Expected AI Command output would generate:
# ------------------------------------
# def connect_to_snowflake():
#     """Establish connection to Snowflake."""
#     logger.info("Connecting to Snowflake...")
#     try:
#         conn = snowflake.connector.connect(
#             user=os.getenv('SNOWFLAKE_USER'),
#             password=os.getenv('SNOWFLAKE_PASSWORD'),
#             account=os.getenv('SNOWFLAKE_ACCOUNT'),
#             warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
#             database=os.getenv('SNOWFLAKE_DATABASE'),
#             schema=os.getenv('SNOWFLAKE_SCHEMA')
#         )
#         logger.info("Successfully connected to Snowflake")
#         return conn
#     except Exception as e:
#         logger.error(f"Error connecting to Snowflake: {e}")
#         raise
# ------------------------------------
# 
# VIDEO NARRATION: "Warp's AI Command generates a complete connection function with proper
# error handling. The multi-line editing capability makes it easy to review and modify 
# this complex function before adding it to my script."


# DEMO SECTION 3: Sample Data Generation
# In Warp, use AI Command and type:
# "Create a function to generate sample sales data using pandas with transaction_id, date, product, region, quantity, price, and customer_id"
# 
# Expected AI Command output would generate something like:
# ------------------------------------
# def generate_sample_data(num_rows=1000):
#     """Generate sample sales data for demonstration."""
#     logger.info(f"Generating sample dataset with {num_rows} rows...")
#     
#     # Create random data
#     np.random.seed(42)
#     
#     # Generate sample dates
#     start_date = pd.Timestamp('2023-01-01')
#     end_date = pd.Timestamp('2023-12-31')
#     date_range = pd.date_range(start=start_date, end=end_date, periods=num_rows)
#     
#     products = ['Widget A', 'Widget B', 'Gadget X', 'Gadget Y', 'Tool Z']
#     regions = ['North', 'South', 'East', 'West', 'Central']
#     
#     data = {
#         'transaction_id': range(1, num_rows + 1),
#         'transaction_date': date_range,
#         'product': np.random.choice(products, size=num_rows),
#         'region': np.random.choice(regions, size=num_rows),
#         'quantity': np.random.randint(1, 50, size=num_rows),
#         'price': np.round(np.random.uniform(10, 1000, size=num_rows), 2),
#         'customer_id': np.random.randint(1000, 9999, size=num_rows)
#     }
#     
#     # Calculate total_amount
#     df = pd.DataFrame(data)
#     df['total_amount'] = df['quantity'] * df['price']
#     
#     logger.info("Sample dataset created successfully")
#     return df
# ------------------------------------
#
# VIDEO NARRATION: "With complex data generation logic like this, Warp's syntax highlighting
# makes it easy to spot any errors. I can also use the command block feature to collapse 
# this section when I want to focus on other parts of my script."


# DEMO SECTION 4: Creating Snowflake Table
# In Warp, use AI Command and type:
# "Write a function to create a staging table in Snowflake for sales data"
# 
# Expected AI Command output:
# ------------------------------------
# def create_staging_table(conn):
#     """Create a staging table in Snowflake if it doesn't exist."""
#     logger.info("Creating staging table if it doesn't exist...")
#     cursor = conn.cursor()
#     
#     create_table_sql = """
#     CREATE TABLE IF NOT EXISTS sales_staging (
#         transaction_id INTEGER,
#         transaction_date DATE,
#         product VARCHAR(255),
#         region VARCHAR(50),
#         quantity INTEGER,
#         price FLOAT,
#         total_amount FLOAT,
#         customer_id INTEGER,
#         upload_timestamp TIMESTAMP
#     )
#     """
#     
#     try:
#         cursor.execute(create_table_sql)
#         logger.info("Staging table created or already exists")
#     except Exception as e:
#         logger.error(f"Error creating staging table: {e}")
#         raise
#     finally:
#         cursor.close()
# ------------------------------------
#
# VIDEO NARRATION: "Notice how Warp handles the SQL query with proper syntax highlighting,
# making it much easier to read compared to a traditional terminal. I can also use
# Warp's history to recall this command later if I need to modify the table structure."


# DEMO SECTION 5: Upload Function 
# In Warp, use AI Command and type:
# "Create a function to upload a pandas DataFrame to the Snowflake staging table"
# 
# Expected AI Command output:
# ------------------------------------
# def upload_to_snowflake(conn, df):
#     """Upload pandas DataFrame to Snowflake."""
#     logger.info(f"Uploading {len(df)} rows to Snowflake...")
#     
#     # Add upload timestamp
#     df['upload_timestamp'] = datetime.now()
#     
#     # Prepare the data as a list of tuples
#     records = df.to_records(index=False)
#     rows = [tuple(x) for x in records]
#     
#     # Insert data into Snowflake
#     cursor = conn.cursor()
#     
#     try:
#         insert_sql = """
#         INSERT INTO sales_staging (
#             transaction_id, transaction_date, product, region, 
#             quantity, price, total_amount, customer_id, upload_timestamp
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         
#         # Execute many to efficiently insert all rows
#         cursor.executemany(insert_sql, rows)
#         conn.commit()
#         
#         # Get count of rows inserted
#         cursor.execute("SELECT COUNT(*) FROM sales_staging")
#         count = cursor.fetchone()[0]
#         
#         logger.info(f"Successfully loaded data. Total rows in table: {count}")
#     except Exception as e:
#         logger.error(f"Error uploading data: {e}")
#         conn.rollback()
#         raise
#     finally:
#         cursor.close()
# ------------------------------------
#
# VIDEO NARRATION: "For complex database operations like this, Warp's AI Command saves
# me from having to write all this boilerplate code by hand. The rich terminal display
# also makes it easy to read the output when I run this script."


# DEMO SECTION 6: Main Function
# In Warp, use AI Command and type:
# "Write a main function that connects to Snowflake, generates sample data, creates a staging table, and uploads the data"
# 
# Expected AI Command output:
# ------------------------------------
# def main():
#     """Main function to orchestrate the data upload process."""
#     logger.info("Starting Snowflake data upload process")
#     
#     try:
#         # Connect to Snowflake
#         conn = connect_to_snowflake()
#         
#         # Generate sample data
#         df = generate_sample_data()
#         
#         # Show data preview
#         logger.info("Data preview:")
#         logger.info(f"\n{df.head()}")
#         
#         # Create staging table
#         create_staging_table(conn)
#         
#         # Upload data
#         upload_to_snowflake(conn, df)
#         
#         logger.info("Data upload process completed successfully")
#     except Exception as e:
#         logger.error(f"Error in data upload process: {e}")
#     finally:
#         if 'conn' in locals() and conn:
#             conn.close()
#             logger.info("Snowflake connection closed")
#
# if __name__ == "__main__":
#     main()
# ------------------------------------
#
# VIDEO NARRATION: "With Warp's terminal blocks, each section of this script execution
# is clearly delineated, making it easy to see what's happening at each stage. If I 
# encounter any errors, Warp's improved error formatting makes debugging much easier."


# DEMO SECTION 7: Running the Script
# In Warp, demonstrate:
# 1. Saving the file: echo "Script saved as snowflake_upload.py"
# 2. Running the script: python snowflake_upload.py
# 3. Show how Warp's command execution indicators make it clear when the script is running
#
# VIDEO NARRATION: "When running data engineering scripts like this, Warp's command
# execution indicators make it clear when long-running processes are still executing.
# After running the script, I can easily find it in my command history if I need to
# run it again or modify it."


# DEMO SECTION 8: Follow-up Commands
# In Warp, use AI Command and type:
# "Show me Snowflake SQL commands to verify data was uploaded correctly"
# 
# Expected AI Command output:
# ------------------------------------
# # Connect to Snowflake using SnowSQL
# snowsql -c my_connection
# 
# # Count rows in the staging table
# SELECT COUNT(*) FROM sales_staging;
# 
# # View sample data
# SELECT * FROM sales_staging LIMIT 10;
# 
# # Check data distribution by region
# SELECT region, COUNT(*) as count, SUM(total_amount) as total_sales
# FROM sales_staging
# GROUP BY region
# ORDER BY total_sales DESC;
# ------------------------------------
#
# VIDEO NARRATION: "Warp's AI Command feature is also helpful for generating follow-up
# commands and queries. Instead of having to remember Snowflake SQL syntax, I can just
# ask the AI to generate the queries I need."


# CONCLUSION FOR VIDEO:
# "As you can see, Warp's AI Command feature dramatically speeds up the development
# of data engineering scripts. Instead of having to remember all the syntax details or
# search for examples online, I can generate solid, working code snippets directly in 
# my terminal. Combined with Warp's other features like command blocks, rich output,
# and improved error formatting, it makes data engineering workflows much more efficient."

