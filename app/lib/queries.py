import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
PG_DATABASE =  os.getenv('PG_DATABASE')

def db_connect():
	try:
		connection = psycopg2.connect(
			user=PG_USER,
			password=PG_PASSWORD,
			host=PG_HOST,
			port=PG_PORT,
			database=PG_DATABASE
		)
		
		cursor = connection.cursor()

		return connection, cursor

	except (Exception, psycopg2.Error) as error :
		print("Failed to connect, error")

def db_close(connection, cursor):
	try:
		cursor.close()
		connection.close()

	except (Exception, psycopg2.Error) as error :
		print("Failed to close connection, error")

def validate_user(user, password):
	connection, cursor = db_connect()
	params = (user, password)

	query = '''
	 SELECT id 
     FROM users.credentials
     WHERE username = %s
     AND password = crypt(%s, password);
    '''

	cursor.execute(query, params)
	count = cursor.rowcount
	db_close(connection, cursor)

	if count >= 1:
		return True
	else:
		return False