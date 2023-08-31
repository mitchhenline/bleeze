"""Bleeze Server"""

from flask import Flask, render_template
from jinja2 import StrictUndefined
from model import connect_to_db

app = Flask(__name__)
app.secret_key = "selfstorage"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def store_select():
    """View store selector."""
    return render_template("store_selector.html")
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)