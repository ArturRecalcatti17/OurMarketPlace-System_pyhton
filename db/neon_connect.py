import os
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv('DATABASE_URL')

connection_pool = pool.SimpleConnectionPool(
    2,
    10,
    connection_string
)

if connection_pool:
    print('sucesso')

conn = connection_pool.getconn()