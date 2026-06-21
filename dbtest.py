import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="K@thrigupp1",
    database="urlshortener"
)

cursor = db.cursor()

cursor.execute(
    """
    INSERT INTO urls(short_url,long_url)
    VALUES(%s,%s)
    """,
    ("abc123","https://google.com")
)

db.commit()

db.close()