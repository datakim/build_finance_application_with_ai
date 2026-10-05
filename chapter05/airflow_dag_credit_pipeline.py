# Listing 5.2 (chapter 5): A minimal Airflow DAG for BFSI monthly merges.
#
# Difference from the printed listing: the book imports
#     from airflow.providers.postgres.operators.postgres import PostgresOperator
# which was removed in apache-airflow-providers-postgres 6.0.0. This file uses the
# generic SQLExecuteQueryOperator from the common.sql provider instead, so the
# operator keyword is conn_id= rather than postgres_conn_id=. Everything else is
# as printed.
#
# Setup (appendix A: install Airflow in its own virtual environment):
#   pip install "apache-airflow==3.1.7" apache-airflow-providers-postgres \
#     --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.1.7/constraints-3.12.txt
#   - Copy this file and the sql/ folder into your Airflow dags folder; the sql=
#     paths are resolved relative to this file.
#   - Create a Postgres connection with the id "bfsidb".
#   - sql/credit_data_mart.sql is listing 5.1. The other three scripts
#     (create_monthly_usage.sql, create_bureau_lookup.sql, create_demographics.sql)
#     are not printed in the book; supply your own.
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

default_args = {
    "owner": "credit_pipeline",
    "start_date": datetime(2024, 1, 1),
    "depends_on_past": False,
    "retries": 1
}

with DAG(
    dag_id="credit_pipeline_dag",
    default_args=default_args,
    schedule="@monthly",
    catchup=False
) as dag:

    monthly_usage = SQLExecuteQueryOperator(
        task_id="create_monthly_usage",
        sql="sql/create_monthly_usage.sql",
        conn_id="bfsidb"
    )

    bureau_lookup = SQLExecuteQueryOperator(
        task_id="create_bureau_lookup",
        sql="sql/create_bureau_lookup.sql",
        conn_id="bfsidb"
    )

    demographics = SQLExecuteQueryOperator(
        task_id="create_demographics",
        sql="sql/create_demographics.sql",
        conn_id="bfsidb"
    )

    credit_data_mart = SQLExecuteQueryOperator(
        task_id="create_credit_data_mart",
        sql="sql/credit_data_mart.sql",
        conn_id="bfsidb"
    )

monthly_usage >> bureau_lookup >> demographics >> credit_data_mart
