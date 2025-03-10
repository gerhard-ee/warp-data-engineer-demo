# Recreating the Warp Data Engineering Demo Repository

This guide provides step-by-step instructions on how to recreate this data engineering project repository using Warp Terminal and AI prompts. Follow along to learn how to leverage Warp's AI capabilities to build a complete data engineering environment from scratch.

## Prerequisites

- [Warp Terminal](https://www.warp.dev/) installed
- [Git](https://git-scm.com/downloads) installed
- [GitHub CLI](https://cli.github.com/) installed (optional, but recommended)
- A GitHub account
- Basic familiarity with terminal commands

## Project Overview

This repository demonstrates a modern data engineering setup with the following components:

- ETL pipeline scripts for data extraction, transformation, and loading
- Data validation and quality checking tools
- Configuration templates for popular data tools (Snowflake, Airflow)
- Workflow definitions for orchestrating data pipelines
- Sample data files for testing and demonstration
- Comprehensive documentation

## Step-by-Step Recreation Guide

### Step 1: Set Up Your Project Directory

Open Warp Terminal and start with this prompt:

```
Create a new directory structure for a data engineering project with folders for data (raw and processed), scripts, documentation, and resources.
```

Execute the commands provided by the AI:

```bash
mkdir -p warp-data-engineer-demo/{data/{raw,processed},scripts/utils,documentation,resources/warp_workflows}
cd warp-data-engineer-demo
```

### Step 2: Initialize Git Repository

Use this Warp AI prompt:

```
Initialize a git repository in this directory and create a comprehensive .gitignore file suitable for a data engineering project with Python scripts, sensitive credentials, and large data files.
```

The AI will help you:
- Initialize git with `git init`
- Create a detailed .gitignore file covering Python artifacts, data files, credentials, logs, etc.

### Step 3: Create Project README

Use this prompt:

```
Create a README.md file for my data engineering project that explains the purpose, structure, and how to get started.
```

The AI will generate a README.md with:
- Project overview
- Directory structure explanation
- Setup instructions
- Usage examples

### Step 4: Create ETL Scripts

Break this into multiple prompts for better results:

```
Create a Python ETL pipeline script that defines the overall orchestration process, including extract, transform, and load functions.
```

This will create your `scripts/etl_pipeline.py` file.

Next prompt:

```
Create Python scripts for data processing and validation with functions for cleaning, transforming, and validating data before loading.
```

This will create:
- `scripts/data_processing.py`
- `scripts/data_validation.py`

Finally:

```
Create Python utility modules with helper functions for file operations, logging, and configuration management.
```

This will create:
- `scripts/utils/helpers.py`
- `scripts/utils/__init__.py`

### Step 5: Create Configuration Templates

Use this prompt:

```
Create Snowflake configuration template with placeholders for account, username, password, warehouse, database, schema, and role.
```

Follow with:

```
Create an Airflow configuration template with placeholders for connections, DAG settings, operators, and variables.
```

These prompts will create:
- `scripts/snowflake_config_template.json`
- `scripts/airflow_config_template.json`

### Step 6: Create Documentation

Use these prompts:

```
Create an architecture.md file documenting the data pipeline architecture, components, and data flow.
```

And:

```
Create a setup.md file with instructions for setting up the project, installing dependencies, and configuring connections.
```

These will create:
- `documentation/architecture.md`
- `documentation/setup.md`

### Step 7: Create Workflow Definitions

Use this prompt:

```
Create a YAML workflow definition file for Snowflake data pipelines with tasks for data ingestion, transformation, and quality checks.
```

This will create:
- `resources/warp_workflows/snowflake_workflows.yaml`

And:

```
Create a config.json file with general project configuration settings.
```

This will create:
- `resources/config.json`

### Step 8: Generate Sample Data

Use this prompt:

```
Generate a sample CSV sales dataset with fields for transaction_id, date, customer_id, product_id, quantity, price, total, store_id, and region.
```

This will create:
- `data/raw/sample_sales_data.csv`

And:

```
Create a small example_data.csv file that demonstrates the data structure after processing.
```

This will create:
- `data/example_data.csv`

### Step 9: Create GitHub Repository

Use this prompt:

```
Help me create a new public GitHub repository for my data engineering project, commit all my files, and push to GitHub.
```

The AI will guide you through:
1. Using GitHub CLI to create a repository
2. Adding GitHub as a remote
3. Committing all files with a meaningful message
4. Pushing to GitHub

## Detailed Component Explanations

### ETL Pipeline Architecture

The ETL pipeline in this project follows a modular design with separation of concerns:

**Extract**: Sources data from CSV files, databases, or APIs
```python
# Example extract function from etl_pipeline.py
def extract_data(source_path, config):
    """Extract data from the specified source."""
    if source_path.endswith('.csv'):
        return pd.read_csv(source_path)
    elif source_path.endswith('.json'):
        return pd.read_json(source_path)
    # Add more extractors as needed
```

**Transform**: Cleans, validates, and structures the data
```python
# Example from data_processing.py
def transform_sales_data(df):
    """Transform sales data for analytics."""
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Convert date strings to datetime objects
    df['date'] = pd.to_datetime(df['date'])
    
    # Calculate derived fields
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
    return df
```

**Load**: Writes processed data to target destinations
```python
# Example load function
def load_to_snowflake(df, table_name, config):
    """Load dataframe to Snowflake table."""
    conn = create_snowflake_connection(config)
    # Use snowflake connector to write data
    # ...
```

### Configuration Management

The project uses a template-based approach for configuration:

```json
{
    "account": "{{your_account_identifier}}",
    "user": "{{your_username}}",
    "password": "{{your_password}}",
    "warehouse": "COMPUTE_WH",
    "database": "DEMO_DB",
    "schema": "PUBLIC",
    "role": "ACCOUNTADMIN"
}
```

Best practices implemented:
- Placeholder values instead of hardcoded credentials
- Separation of configuration from business logic
- Environment-specific configuration capability

### Workflow Orchestration

Workflows are defined in YAML for readability and maintainability:

```yaml
# Example from snowflake_workflows.yaml
workflows:
  - name: data_ingestion
    description: "Ingest data from raw sources to Snowflake landing zone"
    tasks:
      - name: create_landing_tables
        type: sql
        file: "sql/create_landing_tables.sql"
```

This approach allows:
- Clear definition of tasks, dependencies, and schedules
- Easy modification without changing code
- Documentation of the pipeline flow

## Best Practices for Data Engineering with Warp

### Leveraging AI for Code Generation

When using Warp's AI features for data engineering tasks:

1. **Be Specific**: Provide detailed context in your prompts
   ```
   # Less effective
   "Create a data processing script"
   
   # More effective
   "Create a Python data processing script that handles CSV cleaning with pandas, 
   including handling null values, date formatting, and outlier detection"
   ```

2. **Iterate**: Build your solution step by step
   ```
   # First prompt
   "Create the basic structure of an ETL pipeline script"
   
   # Follow-up prompt
   "Now add error handling and logging to the ETL pipeline"
   ```

3. **Request Explanations**: Ask the AI to explain its code
   ```
   "Explain how the data validation function is checking for data quality issues"
   ```

### Code Organization

1. **Modular Design**: Break functionality into separate modules
   ```
   # Instead of one large script:
   scripts/
   ├── etl_pipeline.py     # Main orchestration
   ├── extractors/         # Data source specific extractors  
   ├── transformers/       # Data transformation logic
   ├── loaders/            # Target-specific loading logic
   └── utils/              # Shared utilities
   ```

2. **Configuration Separation**: Keep configuration separate from code
   ```
   # Environment-specific configs
   config/
   ├── dev.json
   ├── test.json
   └── prod.json
   ```

3. **Function-First Approach**: Write functions with clear inputs and outputs
   ```python
   # Good
   def clean_customer_data(df):
       """Clean customer data by removing duplicates and formatting."""
       # Implementation
       return cleaned_df
   
   # Avoid
   # Large scripts with inline processing
   ```

### Security Best Practices

1. **Never commit credentials**: Use environment variables or secret management
   ```python
   # Use environment variables
   import os
   password = os.environ.get('SNOWFLAKE_PASSWORD')
   ```

2. **Templates over actual configs**: Commit templates, not actual config files
   ```
   # Commit: snowflake_config_template.json
   # Don't commit: snowflake_config.json
   ```

3. **Comprehensive .gitignore**: Prevent accidental credential commits
   ```
   # .gitignore entries
   *.env
   *credentials*
   *.pem
   *.key
   ```

### Warp-Specific Tips for Data Engineers

1. **Create Warp Workflows** for common data tasks:
   - Data extraction commands
   - Database connection snippets
   - Pipeline execution commands

2. **Use AI to Debug**: When errors occur, select the error text and ask Warp AI:
   ```
   "What's causing this error in my Python pandas code and how can I fix it?"
   ```

3. **Command History with Context**: Use Warp's history features to maintain context about your data pipelines

4. **Split Terminal for Monitoring**: Use split terminals to run and monitor data pipelines simultaneously

## Conclusion

By following this guide, you've recreated a complete data engineering project that demonstrates best practices for:
- Modular code organization
- Secure configuration management
- Pipeline orchestration
- Data quality validation
- Documentation

Continue exploring and extending the repository by adding:
- More data sources
- Advanced transformations
- Dashboarding connections
- CI/CD integration
- Containerization

Happy data engineering with Warp!

