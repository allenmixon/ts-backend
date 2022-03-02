import psycopg2

def validate_user(user, password):
	if password == "starchild":
		return True
	else:
		return False

