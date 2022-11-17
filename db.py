import pyodbc

import config


def get_connection() -> pyodbc.Connection:
    """
    generates connection instance using database configuration
    :return: pyodbc connection instance
    """
    driver_str = f'DRIVER={{{config.DB_DRIVER}}}'
    server_str = f'SERVER={config.DB_HOST}'
    database_str = f'DATABASE={config.DB_NAME}'
    user_str = f'UID={config.DB_USER}'
    pwd_str = f'PWD={config.DB_PASSWORD}'
    cert_str = 'TrustServerCertificate=yes'

    connection_str = ";".join([driver_str, server_str, database_str, user_str, pwd_str, cert_str])
    connection = pyodbc.connect(connection_str)
    return connection
