# Warp AI Prompts for Data Engineering Demo Project

This document contains repeatable prompts for use with Warp's AI Command feature to recreate a data engineering demonstration project. Each prompt is designed to generate specific components of the project, and they can be used in sequence to build the complete demo.

## Project Setup

### Project Structure
```
Create a new directory structure for a data engineering project with the following folders: scripts, data/raw, and logs
```

### Requirements File
```
Create a requirements.txt file for a Python data engineering project that will process data and upload it to Snowflake. Include packages for data manipulation, Snowflake connectivity, logging, and environment variable management.
```

### Environment File Template
```
Create a template .env file with placeholders for Snowflake connection parameters including account, username, password, warehouse, database, and schema.
```

## Data Components

### Sample Data Creation
```
Create a sample CSV file named 'sample_sales_data.csv' with the following columns: transaction_id, date, product, region, quantity, price, customer_id. Include 10 rows of realistic sales data across different regions.
```

### Data Transformation Script
```
Create a Python script that reads the sample_sales_data.csv, performs data cleaning, adds derived columns like total_sales (quantity * price), and prepares it for upload to a data warehouse. Include error handling and logging.
```

## Database Integration

### Basic Snowflake Upload Script
```
Create a Python script that demonstrates connecting to Snowflake and uploading data with clear demonstration sections. Each section should be preceded by comments that explain what Warp AI command to use and what the expected output should be. Include sections for importing libraries, connecting to Snowflake, data transformation, and uploading to Snowflake.
```

## Workflow and Orchestration

### Sample Airflow DAG
```
Create a sample Airflow DAG Python file that orchestrates the execution of the data processing and Snowflake upload scripts. Include scheduling parameters and task dependencies.
```

## Quality Assurance

### Testing Framework
```
Create a simple testing framework with pytest for the data processing functions to ensure data quality and transformation accuracy.
```

## Documentation

### README File
```
Create a comprehensive README.md file for a data engineering demonstration project that explains the project structure, how to set up the environment, and how to run the scripts. Include a section on how to use Warp's AI Command for interactive demonstrations.
```

## Demonstration Materials

### Demonstration Script
```
Create a demonstration script that shows how to use Warp's AI Command to generate code snippets for common data engineering tasks like connecting to databases, transforming data, and scheduling tasks. Include detailed comments about what to type as prompts and how to narrate the demonstration.
```

## Using These Prompts

1. Copy the desired prompt from this document
2. Paste it into Warp's AI Command interface (Cmd+K or Ctrl+K)
3. Review and execute the generated commands or code

These prompts are designed to be modular - you can use them independently to generate specific components or sequentially to build the entire project.

