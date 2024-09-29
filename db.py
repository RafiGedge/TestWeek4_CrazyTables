import psycopg2


def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname="wwii_missions",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None


def close_db_connection(conn):
    if conn:
        conn.close()
