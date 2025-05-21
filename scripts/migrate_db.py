import psycopg2

def migrate_data(source_url, target_url):
    # Connect to the source database
    source_conn = pycopg2.connect(source_url)
    source_cursor = source_conn.cursor()

    # Connect to the target database
    target_conn = pycopg2.connect(target_url)
    target_cursor = target_conn.cursor()

    # Fetch data from the source database
    source_cursor.execute("SELECT * FROM your_table")
    rows = source_cursor.fetchall()

    # Insert data into the target database
    for row in rows:
        target_cursor.execute("INSERT INTO your_table VALUES (%s, %s)", row)

    # Commit changes and close connections
    target_conn.commit()
    source_conn.close()
    source_cursor.close()
    target_cursor.close() 
    target_conn.close()

    if __name__ == "__main__":
        source_url = "postgresql://user:password@172.20.202.74:5432/source_db"
        target_url = "postgresql://appuser:1111111111@app-db.ccni6mmgs4z1.us-east-1.rds.amazonaws.com:5432"
        migrate_data(source_url, target_url)