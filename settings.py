DEBUG_ENABLED = False
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

USER_AUTH_DATA = {
    "table": "Employees",
    "identifier": "email",
    "password": "password",
}

SQL_SCRIPTS = [
    "create_tables.sql",
    "populate_database.sql"
]