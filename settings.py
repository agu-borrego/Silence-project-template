LOG_LEVEL = "PRUEBA"
DEBUG_ENABLED = True
HTTP_PORT = 9999
API_PREFIX = "/api"

RUN_API = True
RUN_WEB = True

DB_CONN = {
    "host": "localhost",
    "port": 3306,
    "username": "silence",
    "password": "123456",
    "database": "app",
}

SQL_SCRIPTS = [
    "create_tables.sql",
    "populate_database.sql"
]