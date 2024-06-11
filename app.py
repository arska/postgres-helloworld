"""Hello world from a PostgreSQL server"""

import os
from flask import Flask
import psycopg2

APP = Flask(__name__)  # Standard Flask app


@APP.route("/")
def hello():
    """
    Hello world on root path
    """
    with psycopg2.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            return cur.fetchone()


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=os.environ.get('listenport', 8080))
