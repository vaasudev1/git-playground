from flask import Flask
from flask import request
from flask import redirect
from converter import convert
from sig import signature
import mysql.connector
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="K@thrigupp1",
        database="urlshortener"
    )
cursor = db.cursor()
cursor.execute("select * from urls")
rows = cursor.fetchall()
urls = {}
for row in rows:
    urls[row[0]] = row[1]
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>URL Shortener</h1>

    <form action="/shorten" method="post">
        <input type="text" name="url">
        <input type="submit" value="Shorten">
    </form>
    
    <h2>Redirect</h2>
   
    <form action="/redirect" method="post">
        <input type="text" name="short">
        <input type="submit" value="Redirect">
        </form>
    """
   

@app.route("/shorten", methods=["POST"])
def shorten():
    cursor.execute("select value from counter")
    counter = cursor.fetchone()[0]

    url = request.form["url"]

    count = "".join(convert(counter,62))

    sig = signature("my_secret_key", url)

    sig62 = "".join(convert(sig,62))

    short = count + "." + sig62

    counter += 1
    
    cursor.execute(
        """
        UPDATE counter
        SET value = %s
        """
    , (counter,))

    

    cursor.execute(
        """
        INSERT INTO urls(short_url,long_url)
        VALUES(%s,%s)
        """,
        (short,url)
    )

    urls[short] = url

    db.commit()

    return short

@app.route("/redirect", methods=["POST"])
def redir():
    short = request.form["short"]
    if short in urls:
        return redirect(urls[short])
    return "URL not found"

if __name__ == "__main__":
    app.run(debug=True)