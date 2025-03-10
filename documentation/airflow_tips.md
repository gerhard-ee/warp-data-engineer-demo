# Airflow Tips for Data Engineers

This document provides tips and best practices for managing Apache Airflow in data engineering workflows, with a focus on how Warp terminal's features can enhance your productivity.

## Table of Contents
- [DAG Design Best Practices](#dag-design-best-practices)
- [Task Management](#task-management)
- [Airflow CLI Commands](#airflow-cli-commands)
- [Debugging and Troubleshooting](#debugging-and-troubleshooting)
- [Performance Optimization](#performance-optimization)
- [Working with Airflow in Warp](#working-with-airflow-in-warp)

## DAG Design Best Practices

### Structuring Your DAGs
- **Keep DAGs Simple**: Design DAGs with a single purpose and avoid overly complex workflows
- **Be Explicit**: Clearly define dependencies with `set_upstream()` or `set_downstream()` rather than bitshift operators
- **Dynamic DAG Generation**: Use factory patterns for generating similar DAGs programmatically

```python
# Example of a well-structured factory pattern for dynamic DAG generation
def create_data_pipeline_dag(source, destination, schedule):
    dag = DAG(
        f'data_pipeline_{source}_to_{destination}',
        schedule_interval=schedule,
        catchup=False
    )
    
    with dag:
        extract = PythonOperator(...)
        transform = PythonOperator(...)
        load = PythonOperator(...)
        
        extract >> transform >> load
    
    return dag

# Generate multiple DAGs
for source, destination, schedule in config_data:
    globals()[f'dag_{source}_{destination}'] = create_data_pipeline_dag(source, destination, schedule)
```

### Idempotence
- Design tasks to be idempotent (can be run multiple times without side effects)
- Use appropriate sensors to wait for external conditions instead of time-based waits
- Implement proper error handling with retries and timeouts

### Task Dependencies
- Use task groups for logical organization of related tasks
- Implement clear branching logic with BranchPythonOperator or TaskFlow API
- Consider using SubDAGs for reusable patterns but be aware of executor limitations

## Task Management

### Effective Task Design
- Keep tasks atomic and focused on single responsibilities
- Externalize business logic to importable modules outside of DAG files
- Use appropriate operator types for different tasks (PythonOperator, BashOperator, etc.)

### Sensors vs Polling
- Use sensors for external dependencies (Filesensors, ExternalTaskSensor)
- Set appropriate timeouts and poke intervals
- Consider using smart sensors for reduced resource consumption

### Best Practices for Different Operators
- **PythonOperator**: Pass data between tasks using XComs sparingly
- **BashOperator**: Prefer absolute paths and proper error handling
- **Custom Operators**: Create them for reusable, common patterns specific to your organization

## Airflow CLI Commands

### Essential CLI Commands
```bash
# Start the Airflow webserver
airflow webserver --port 8080

# Start the Airflow scheduler
airflow scheduler

# List all DAGs
airflow dags list

# Pause/unpause a DAG
airflow dags pause dag_id
airflow dags unpause dag_id

# Trigger DAG run
airflow dags trigger dag_id

# Get DAG runs information
airflow dags list-runs -d dag_id

# Test a specific task
airflow tasks test dag_id task_id date
```

### Maintenance Commands
```bash
# Clear task instances
airflow tasks clear dag_id -t task_id -s YYYY-MM-DD -e YYYY-MM-DD

# Backfill a DAG
airflow dags backfill dag_id -s YYYY-MM-DD -e YYYY-MM-DD

# Cleanup old logs
airflow db clean
```

## Debugging and Troubleshooting

### Common Issues and Solutions
- **Task failures**: Check logs using `airflow tasks logs dag_id task_id run_id`
- **Scheduler issues**: Check scheduler logs and ensure it has sufficient resources
- **Database performance**: Monitor database connections and consider scaling if needed

### Effective Debugging Techniques
- Test tasks in isolation using `airflow tasks test`
- Use proper logging within tasks
- Implement monitoring and alerting for critical DAGs

## Performance Optimization

### Resource Management
- Set appropriate parallelism, dag_concurrency, and max_active_runs
- Use pools to limit concurrent resource-intensive tasks
- Consider scaling out the executor (Celery, Kubernetes) for large deployments

### Database Optimization
- Regularly run `airflow db clean` to remove old logs and metadata
- Set appropriate task retention periods
- Consider sharding for very large Airflow deployments

## Working with Airflow in Warp

### Leveraging Warp's Features

#### Command History and Blocks
- Warp's block-based interface makes it easy to distinguish between different Airflow command outputs
- Use Warp's powerful history search (Ctrl+R) to quickly find previous Airflow commands
- Pin commonly used Airflow commands for quick access

#### Warp AI Assistant
- Ask Warp AI to help debug Airflow task failures: "Why is my task failing with this error?"
- Generate complex Airflow CLI commands: "Show me how to backfill a DAG for the last 3 days"
- Get explanations for Airflow concepts: "Explain Airflow's XCom and when to use it"

#### Workflow Enhancement
- Use Warp's split panes to:
  - Monitor logs in one pane while editing DAG code in another
  - Run the scheduler in one pane while testing tasks in another
  - View webserver output while running CLI commands

#### Tips for Effective Terminal Management
- Create separate blocks for different Airflow components (scheduler, webserver)
- Use Warp themes to color-code different environments (dev, staging, prod)
- Leverage Warp's AI to:
  - Generate or explain complex Airflow cron expressions
  - Help with Python operator syntax and best practices
  - Debug task failures by analyzing log outputs

### Example: Working with Multiple Airflow Environments

Warp's workflow for managing multiple Airflow environments:

1. Set up environment variables for different Airflow instances
   ```bash
   # In one Warp block
   export AIRFLOW_HOME=/path/to/dev/airflow
   airflow webserver

   # In another Warp block
   export AIRFLOW_HOME=/path/to/prod/airflow
   airflow dags list
   ```

2. Use Warp's split panes to monitor multiple environments simultaneously
3. Label blocks with environment names for clear organization
4. Save common Airflow command sequences as reusable workflows

### Time-saving Warp + Airflow Tricks

- **Quick Testing**: Set up a Warp workflow that combines:
  ```bash
  # Test task
  airflow tasks test dag_id task_id $(date -d "yesterday" +%Y-%m-%d)
  
  # Then immediately check logs if needed
  airflow tasks logs dag_id task_id $(date -d "yesterday" +%Y-%m-%d)
  ```

- **Monitoring DAGs**: Create a refresh command to watch DAG status:
  ```bash
  # Refresh every 5 seconds
  watch -n 5 "airflow dags list-runs -d important_dag_id"
  ```
  
- Use Warp blocks to maintain context between different troubleshooting steps

