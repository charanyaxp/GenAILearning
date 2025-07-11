"""This module will have utilities
"""
from dotenv import load_dotenv
import os
import mysql.connector
from typing import Union

def get_database_connection(): 
    """This method connects to the mysql database

    Returns:
        Union[PooledMySQLConnection, MySQLConnectionAbstract]: _description_
    """
    load_dotenv()
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
    return connection
