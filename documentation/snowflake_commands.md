# Snowflake CLI Commands for Data Engineers

This documentation covers essential Snowflake commands that data engineers commonly use in their workflows. Each section includes examples and explanations to help you navigate Snowflake's command-line interface (Snow CLI) effectively.

## Table of Contents
- [Connection Commands](#connection-commands)
- [Data Loading](#data-loading)
- [Query Execution](#query-execution)
- [Table Management](#table-management)
- [User and Role Management](#user-and-role-management)
- [Performance Optimization](#performance-optimization)

## Connection Commands

### Connecting to Snowflake using Snow CLI

```bash
# Basic connection with profile
snow sql -c <connection_name>

# Ad hoc connection with parameters
snow sql --account <account_identifier> --username <username> --database <database> --schema <schema> --role <role> --warehouse <warehouse>

# Example:
snow sql --account xy12345.us-east-1 --username dataengineer --database ANALYTICS --schema PUBLIC --role DATA_ENGINEER --warehouse COMPUTE_WH

# Connection using environment variables
export SNOWFLAKE_ACCOUNT=xy12345.us-east-1
export SNOWFLAKE_USER=dataengineer
export SNOWFLAKE_ROLE=DATA_ENGINEER
snow sql
```

### Managing Connection Profiles

```bash
# List all configured connections
snow connection list

# Create a new connection profile
snow connection create <profile_name>

# Set default connection
snow connection set-default <profile_name>
```

### Switching Contexts

```sql
-- Switch to a different database
USE DATABASE analytics;

-- Switch to a different schema
USE SCHEMA reporting;

-- Switch to a different warehouse
USE WAREHOUSE etl_warehouse;

-- Switch to a different role
USE ROLE data_engineer;
```

### Viewing Current Session Information

```sql
-- View current session details
SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE(), CURRENT_SCHEMA(), CURRENT_WAREHOUSE();
```

## Data Loading

### Managing Stages with Snow CLI

```bash
# List files in a stage
snow stage ls @my_stage

# Upload local file to a stage
snow stage copy <local_file_path> @my_stage/

# Download files from a stage
snow stage get @my_stage/data.csv <local_destination>

# Create a new stage
snow sql -q "CREATE OR REPLACE STAGE my_stage;"

# Create external stage (e.g., AWS S3)
snow sql -q "CREATE OR REPLACE STAGE s3_stage URL='s3://mybucket/path/' CREDENTIALS=(AWS_KEY_ID='key' AWS_SECRET_KEY='secret');"
```

### Loading Data from Stage

```sql
-- Copy from stage to table
COPY INTO my_table
FROM @my_stage/data.csv
FILE_FORMAT = (TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1);

-- Load with error handling
COPY INTO my_table
FROM @my_stage/data.csv
FILE_FORMAT = (TYPE = 'CSV')
ON_ERROR = 'CONTINUE'
VALIDATION_MODE = 'RETURN_ERRORS';

-- Load with data transformation
COPY INTO my_table (col1, col2, col3)
FROM (SELECT 
        $1,
        $2::INTEGER,
        TO_TIMESTAMP_NTZ($3)
      FROM @my_stage/data.csv)
FILE_FORMAT = (TYPE = 'CSV');
```

### Unloading Data

```sql
-- Unload data to a stage
COPY INTO @my_stage/output/
FROM my_table
FILE_FORMAT = (TYPE = 'CSV' COMPRESSION = 'GZIP');

-- Unload with specific columns and transformation
COPY INTO @my_stage/output/
FROM (SELECT col1, UPPER(col2), col3::DATE FROM my_table WHERE status = 'active')
FILE_FORMAT = (TYPE = 'PARQUET');
```

### Executing SQL Files

```bash
# Execute a SQL file
snow sql -f path/to/my_queries.sql

# Execute a SQL file with variable substitution
snow sql -f load_data.sql -D DATABASE=analytics -D TABLE=customers
```

## Query Execution

### Executing Queries with Snow CLI

```bash
# Execute a single query and return results
snow sql -q "SELECT * FROM customers LIMIT 10"

# Execute multiple queries
snow sql -q "USE WAREHOUSE COMPUTE_WH; SELECT COUNT(*) FROM orders"

# Execute a query and output results to a file
snow sql -q "SELECT * FROM large_table" -o results.csv
```

### Basic Queries

```sql
-- Select with filtering
SELECT * FROM customer_data WHERE region = 'EAST' LIMIT 100;

-- Aggregations
SELECT 
  region,
  COUNT(*) as customer_count,
  AVG(total_spend) as avg_spend
FROM customer_data
GROUP BY region
ORDER BY avg_spend DESC;

-- Joins
SELECT 
  c.customer_id,
  c.name,
  SUM(o.amount) as total_purchases
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.purchase_date >= DATEADD(month, -3, CURRENT_DATE())
GROUP BY c.customer_id, c.name;
```

### Advanced Queries

```sql
-- Window functions
SELECT 
  region,
  product,
  sales,
  SUM(sales) OVER (PARTITION BY region) as region_sales,
  sales / SUM(sales) OVER (PARTITION BY region) as pct_of_region
FROM sales_data;

-- Pivot tables
SELECT * FROM (
  SELECT region, product, sales FROM sales_data
) PIVOT (
  SUM(sales) FOR product IN ('Product A', 'Product B', 'Product C')
);

-- Common Table Expressions (CTEs)
WITH regional_sales AS (
  SELECT region, SUM(sales) as total_sales
  FROM sales_data
  GROUP BY region
),
top_regions AS (
  SELECT region
  FROM regional_sales
  ORDER BY total_sales DESC
  LIMIT 3
)
SELECT s.*
FROM sales_data s
JOIN top_regions t ON s.region = t.region;
```

## Table Management

### Creating and Modifying Tables

```sql
-- Create a new table
CREATE OR REPLACE TABLE customer_orders (
  order_id NUMBER(38,0),
  customer_id VARCHAR(20),
  order_date DATE,
  amount DECIMAL(12,2),
  status VARCHAR(10)
);

-- Add a column
ALTER TABLE customer_orders ADD COLUMN shipping_address VARCHAR(255);

-- Create a clone of a table
CREATE OR REPLACE TABLE customer_orders_backup CLONE customer_orders;

-- Create a temporary table
CREATE OR REPLACE TEMPORARY TABLE temp_analysis AS
SELECT customer_id, SUM(amount) as total_spent
FROM customer_orders
GROUP BY customer_id;
```

### Table Information and Maintenance

```bash
# Describe a table using Snow CLI
snow sql -q "DESCRIBE TABLE customer_orders"

# Get table schema as JSON
snow object describe --name customer_orders --type table --database ANALYTICS --schema PUBLIC --output json

# Show tables in a schema
snow sql -q "SHOW TABLES IN ANALYTICS.PUBLIC"
```

```sql
-- Resize a table
ALTER TABLE customer_orders RESIZE;

-- Recluster a table
ALTER TABLE customer_orders RECLUSTER;

-- Create a masking policy for sensitive data
CREATE OR REPLACE MASKING POLICY email_mask AS
  (val VARCHAR) RETURNS VARCHAR ->
  CASE
    WHEN CURRENT_ROLE() IN ('ADMIN', 'SECURITY_ADMIN') THEN val
    ELSE REGEXP_REPLACE(val, '^(.)(.*?)(@.*)', '\\1***\\3')
  END;

-- Apply the masking policy
ALTER TABLE customers MODIFY COLUMN email SET MASKING POLICY email_mask;
```

### Managing Constraints and Keys

```sql
-- Add a primary key
ALTER TABLE customers ADD PRIMARY KEY (customer_id);

-- Add a foreign key
ALTER TABLE orders ADD CONSTRAINT fk_customer
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- Add a unique constraint
ALTER TABLE users ADD CONSTRAINT uq_email UNIQUE (email);
```

## User and Role Management

### Managing Users and Roles with Snow CLI

```bash
# List users
snow sql -q "SHOW USERS"

# List roles
snow sql -q "SHOW ROLES"

# Create a new user
snow sql -q "CREATE USER data_analyst PASSWORD = 'strong_password' DEFAULT_ROLE = DATA_ANALYST DEFAULT_WAREHOUSE = ANALYST_WH"

# Grant role to user
snow sql -q "GRANT ROLE etl_operator TO USER data_engineer"
```

### Creating and Managing Users

```sql
-- Create a new user
CREATE USER data_analyst
  PASSWORD = 'strong_password'
  DEFAULT_ROLE = DATA_ANALYST
  DEFAULT_WAREHOUSE = ANALYST_WH;

-- Alter user properties
ALTER USER data_analyst SET DEFAULT_WAREHOUSE = REPORTING_WH;

-- Create a role
CREATE ROLE etl_operator;

-- Grant privileges to role
GRANT USAGE ON WAREHOUSE ETL_WH TO ROLE etl_operator;
GRANT USAGE ON DATABASE RAW_DATA TO ROLE etl_operator;
GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA RAW_DATA.PUBLIC TO ROLE etl_operator;

-- Assign role to user
GRANT ROLE etl_operator TO USER data_engineer;
```

## Performance Optimization

### Warehouse Management

```bash
# List warehouses
snow sql -q "SHOW WAREHOUSES"

# Resume a warehouse
snow sql -q "ALTER WAREHOUSE reporting_wh RESUME"

# Suspend a warehouse
snow sql -q "ALTER WAREHOUSE reporting_wh SUSPEND"
```

```sql
-- Create a new warehouse
CREATE OR REPLACE WAREHOUSE reporting_wh
  WITH WAREHOUSE_SIZE = 'MEDIUM'
  AUTO_SUSPEND = 300
  AUTO_RESUME = TRUE
  INITIALLY_SUSPENDED = TRUE;

-- Resize a warehouse
ALTER WAREHOUSE reporting_wh SET WAREHOUSE_SIZE = 'LARGE';

-- Check warehouse utilization
SELECT 
  warehouse_name,
  start_time,
  end_time,
  credits_used
FROM snowflake.account_usage.warehouse_metering_history
WHERE warehouse_name = 'REPORTING_WH'
AND start_time >= DATEADD(day, -7, CURRENT_DATE())
ORDER BY start_time DESC;
```

### Query Optimization and Monitoring

```bash
# Check query history with Snow CLI
snow sql -q "SELECT query_id, user_name, query_text, execution_time/1000 as execution_time_seconds FROM snowflake.account_usage.query_history LIMIT 10"

# Monitor currently running queries
snow sql -q "SHOW RUNNING QUERIES"

# Cancel a query
snow sql -q "CANCEL QUERY '<query_id>'"
```

```sql
-- View query history
SELECT 
  query_id,
  user_name,
  warehouse_name,
  execution_time/1000 as execution_time_seconds,
  query_text
FROM snowflake.account_usage.query_history
WHERE execution_time > 10000  -- queries taking over 10 seconds
AND query_type = 'SELECT'
ORDER BY execution_time DESC
LIMIT 20;

-- Explain a query execution plan
EXPLAIN
SELECT * FROM large_table
WHERE date_col BETWEEN '2023-01-01' AND '2023-01-31'
AND status = 'COMPLETED';

-- Create a materialized view for faster queries
CREATE OR REPLACE MATERIALIZED VIEW mv_daily_sales AS
SELECT 
  date_trunc('day', order_date) as day,
  product_id,
  SUM(quantity) as units_sold,
  SUM(amount) as total_sales
FROM orders
GROUP BY 1, 2;
```

### Database Objects Management

```bash
# List schemas in a database
snow sql -q "SHOW SCHEMAS IN DATABASE analytics"

# Get information about a specific object
snow object describe --name my_table --type table

# List all objects of a specific type
snow object list --type table --database ANALYTICS --schema PUBLIC
```

---

This documentation covers the most common Snowflake commands using the Snow CLI that data engineers use in their daily work. The Snow CLI is Snowflake's modern command-line tool that replaces the older SnowSQL client.

For more detailed information, refer to the [official Snowflake documentation](https://docs.snowflake.com/en/user-guide/snow-cli).

