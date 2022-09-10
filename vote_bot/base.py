import psycopg2

def open_db():
    conn = psycopg2.connect(
        database="festival_vote_bot",
        user="postgres",
        password="Pauc2173",
        host="localhost",
        port="4803")
    cur = conn.cursor()
    return conn, cur


