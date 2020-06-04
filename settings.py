###############################################################################
# Project-specific settings
###############################################################################

# Shows debug messages while Silence is running
DEBUG_ENABLED = True

# Database connection details
DB_CONN = {
    "host": "localhost",
    "port": 3306,
    "username": "silence",
    "password": "123456",
    "database": "app",
}

# The sequence of SQL scripts located in the sql/ folder that must
# be ran when the 'silence createdb' command is issued
SQL_SCRIPTS = [
    "create_tables.sql",
    "populate_database.sql"
]

# The port in which the API and the web server will be deployed
HTTP_PORT = 8080

# The URL prefix for all API endpoints
API_PREFIX = "/api"

# Table and fields that are used for both login and register
USER_AUTH_DATA = {
    "table": "Employees",
    "identifier": "email",
    "password": "password",
}