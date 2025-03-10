# Warp Terminal Demo: Snowflake Data Uploads & Airflow Workflow Creation

## Project Overview

This project demonstrates how to use Warp terminal to streamline two critical data engineering workflows:

1. **Uploading data to Snowflake** - Showing how Warp's features enhance the experience of preparing and loading data into Snowflake.
2. **Creating and managing Airflow DAGs** - Demonstrating how Warp can improve the process of developing, testing, and deploying Airflow data pipelines.

[Warp](https://www.warp.dev/) is a modern, Rust-based terminal that enhances productivity with features particularly valuable for these data engineering tasks:

- AI command suggestions for Snowflake CLI commands and Airflow operations
- Command blocks for grouping related operations in your ETL process
- Command history with context for easily repeating complex data loading steps
- SSH integration for connecting to Airflow servers
- Syntax highlighting for SQL and Python (DAG) code

## Setup Instructions

### Prerequisites

- macOS, Windows, or Linux machine
- [Warp Terminal](https://www.warp.dev/) installed
- Python 3.8+ for running the demo scripts
- Snowflake account with appropriate access permissions
- Airflow environment (local or remote)
- Snowflake Connector for Python
- Apache Airflow Python package

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/wortel3/warp-data-engineer-demo.git
   cd warp-data-engineer-demo
   ```

2. Set up the Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r scripts/requirements.txt
   ```

3. Configure Snowflake credentials:
   ```bash
   cp scripts/snowflake_config_template.json scripts/snowflake_config.json
   # Edit the file with your Snowflake credentials
   ```

4. Configure Airflow connection (if using remote Airflow):
   ```bash
   cp scripts/airflow_config_template.json scripts/airflow_config.json
   # Edit the file with your Airflow connection details
   ```

## Demo Contents

### 1. Snowflake Data Upload Workflow

- **Data Preparation**
  - Using Warp to preview, clean, and transform CSV data before upload
  - Command blocks to document each preprocessing step
  
- **Snowflake Connection**
  - Setting up and testing Snowflake connection using Warp's environment management
  - Saving connection commands as Warp workflows
  
- **Data Loading**
  - Creating Snowflake tables with the proper schema
  - Using SnowSQL commands to bulk load data
  - Monitoring upload progress with Warp's split-pane feature
  
- **Data Validation**
  - Running SQL queries to validate loaded data
  - Using Warp's history to compare results before and after loading

### 2. Airflow DAG Creation and Management

- **DAG Development**
  - Creating Python DAG files with Warp's code editing capabilities
  - Syntax highlighting and error checking for Airflow DAG code
  
- **DAG Testing**
  - Running local tests of DAG components
  - Using Warp's command blocks to group test results
  
- **DAG Deployment**
  - Deploying DAGs to Airflow environment using SSH
  - Monitoring DAG execution from the terminal
  
- **Workflow Integration**
  - Creating a complete workflow that uploads data to Snowflake and then triggers an Airflow DAG
  - Setting up automation using Warp's workflow feature

### 3. Productivity Tips

- Creating custom Warp workflows for Snowflake operations
- Setting up command aliases for frequent Airflow tasks
- Using AI assistance for troubleshooting data load issues
- Keyboard shortcuts that save time during ETL processes

## Directory Structure

```
warp-data-engineer-demo/
├── scripts/
│   ├── snowflake_upload.py        # Python script for Snowflake data upload
│   ├── create_airflow_dag.py      # Script to generate Airflow DAG
│   ├── requirements.txt           # Python dependencies
│   └── sample_transformations/    # Example data transformation scripts
├── data/
│   ├── raw/                       # Sample raw data files
│   └── processed/                 # Processed data ready for Snowflake
├── dags/
│   └── sample_snowflake_dag.py    # Example Airflow DAG for Snowflake processing
├── resources/
│   └── warp_workflows/            # Saved Warp workflows for demo
└── documentation/
    ├── snowflake_commands.md      # Reference for Snowflake commands
    └── airflow_tips.md            # Tips for Airflow DAG management
```

## Feedback and Contributions

If you have suggestions for improving this demo or want to contribute additional examples for Snowflake uploads or Airflow DAG creation with Warp, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

