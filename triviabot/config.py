import os

# Database connection
db_provider = os.getenv('triviaDBProvider', 'postgres')

# The following will be unpacked as parameters for db.bind()
# See https://docs.ponyorm.com/database.html for the required parameters for each provider
db = {
    'user': os.getenv('triviaDBUser', 'postgres'),
    'password': os.getenv('triviaDBPassword', 'example'),
    'host': os.getenv('triviaDBHost', 'postgres'),
    'port': int(os.getenv('triviaDBPort', '5432')),
    'database': os.getenv('triviaDBDatabase', 'postgres'),
}
