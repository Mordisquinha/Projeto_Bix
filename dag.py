from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.subdag_operator import SubDagOperator
from airflow.contrib.operators.ssh_operator import SSHOperator


stage1 = None
stage2 = None 
stage3 = None

rel = None

def load_subdag_stg(parent_dag_name, child_dag_name):
    global stage1, stage2, stage3

    subdag_stg = DAG(
        dag_id = f'{parent_dag_name}.{child_dag_name}',
        description = f'Subdag {parent_dag_name} da dag {child_dag_name}',
        start_date = start,
        schedule_interval = "0 7 * * *",
        catchup = False   
    )

    with subdag_stg:
        for etapa in ['api.py', 'parquet.py', 'postgress.py']:
            command = f"""
            cd ~/PROJETO_BIX/ETAPA_STG/; sudo python3 {etapa}"""

            if etapa == 'api.py':
                stage1 = SSHOperator(
                    task_id = f'{etapa}'.replace('.py', ''),
                    ssh_conn_id = 'ssh_servidor_bix',
                    command = command,
                    dag = subdag_stg
                )
            if etapa == 'parquet.py':
                stage2 = SSHOperator(
                    task_id = f'{etapa}'.replace('.py', ''),
                    ssh_conn_id = 'ssh_servidor_bix',
                    command = command,
                    dag = subdag_stg
                )
            if etapa == 'postgress.py'.replace('.py', ''):
                stage3 = SSHOperator(
                    task_id = f'{etapa}',
                    ssh_conn_id = 'ssh_servidor_bix',
                    command = command,
                    dag = subdag_stg
                )


    return subdag_stg


def load_subdag_rel(parent_dag_name, child_dag_name):
    global rel 

    subdag_rel = DAG(
        dag_id = f'{parent_dag_name}.{child_dag_name}',
        description = f'Subdag {parent_dag_name} da dag {child_dag_name}',
        start_date = start,
        schedule_interval = "0 7 * * *",
        catchup = False   
    )

    with subdag_rel:
        command = """
            cd ~/PROJETO_BIX/ETAPA_STG/; sudo python3 insert_rel.py"""

        rel = SSHOperator(
            task_id = 'insert_rel',
            ssh_conn_id = 'ssh_servidor_bix',
            command = command,
            dag = subdag_rel
        )

    return subdag_rel



start = datetime.today() - timedelta(days=2)

with DAG(dag_id="ETL_BIX", start_date=start,
        schedule_interval="0 7 * * *" , 
        catchup=False):

    stage = SubDagOperator(
        task_id = 'STAGE',
        subdag = load_subdag_stg(
            parent_dag_name="ETL_BIX",
            child_dag_name="STG"
        )
    )
    
    rel = SubDagOperator(
        task_id = 'RELACIONAL',
        subdag = load_subdag_rel(
            parent_dag_name="ETL_BIX",
            child_dag_name="REL"
        )
    )

stage >> rel

 


