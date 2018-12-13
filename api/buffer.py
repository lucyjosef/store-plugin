#####
#####
##### AVEC PANDAS (mais ça marche pas)
#####
#####
#!flask/bin/python
import json
import time
# import psycopg2
import pandas as pd
from flask import Flask
from flask import request
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('postgresql://admin@localhost:5432/store-plugin')

################ LISTS ################
@app.route('/list', methods=['GET', 'POST'])
def index_list():
    if request.method == 'GET':
        df=pd.read_sql_query('select * from "lists"',con=engine)
        df = df.to_json()
        return df
    elif request.method == 'POST':
        budget = request.form["budget"]
        if ',' in request.form["budget"]:
            budget = budget.replace(',', '.')
        df = pd.DataFrame([{
            'index': None,
            'name' : request.form["name"],
            'budget': budget,
            'created_at': str(time.strftime("%Y-%m-%d"))
        }])
        df.to_sql('lists', con=engine, if_exists='append')
        return 'Your list has been successfully saved !'

@app.route('/list/<int:list_id>', methods=["GET", "DELETE"])
def show_list(list_id):
    if request.method == 'GET':
        return 'json.dumps(res_dict)'
    elif request.method == 'DELETE':
        return 'Your list has been successfully deleted'


################ ITEMS ################

@app.route('/list/<int:list_id>/item', methods=["GET", "POST"])
def index_item(list_id):
    if request.method == 'GET':
        return 'json.dumps(res)'
