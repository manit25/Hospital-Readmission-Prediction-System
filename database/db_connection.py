import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="hospital_db",
        user="postgres",
        password="password"
    )
    return conn