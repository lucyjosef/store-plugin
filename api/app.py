#!flask/bin/python
import json
import psycopg2
from flask import Flask
# from .config import Config

app = Flask(__name__)
conn = psycopg2.connect("dbname=store-plugin user=admin host=localhost")
cur = conn.cursor()

################ LISTS ################
@app.route('/list')
def index():
    cur.execute("""SELECT * FROM lists""")
    res_dict = cur.fetchall()
    return json.dumps(res_dict)
    cur.close()

@app.route('/list/<int:list_id>')
def show(list_id):
    cur.execute("""SELECT * FROM lists WHERE id=""" + str(list_id))
    res_dict = cur.fetchall()
    return json.dumps(res_dict)
