"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch9875ekobicv5sjnk1g-a.oregon-postgres.render.com",
        database="postgre_rac0",
        user="postgre_rac0_user",
        password="IKQUXUvP4mGrhecqvoBQFAs32H25gF4E")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
