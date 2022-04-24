import json

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user_pg:thisisasecurepassword@database_service:3360/db_pg"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return """<h1>Welcome to the Flask service</h1>"""


if __name__ == '__main__':
    app.run()
