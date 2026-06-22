from flask import Flask,abort
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
     """
   

@app.route("/shorten", methods=["POST"])
def shorten():
    cursor.execute("select value from counter")
    counter = cursor.fetchone()[0]

    url = request.form["url"]

    count = "".join(convert(counter,62))

    sig = signature("my_secret_key", count)

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

    return request.host_url + short

@app.route('/<short>',strict_slashes=False)
def redir(short):
    m = short.split(".")
    if("".join(convert(signature("my_secret_key",m[0]),62))!=m[1]):
        abort(404)
    if short in urls:
        return redirect(urls[short])
    abort(404)


if __name__ == '__main__':
    # use_reloader=False stops Flask from restarting when files change
    app.run(debug=True, use_reloader=False)
