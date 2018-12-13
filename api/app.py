#!flask/bin/python
import json
import time
import psycopg2
from flask import Flask
from flask import request

app = Flask(__name__)
conn = psycopg2.connect("dbname=store-plugin user=admin host=localhost")
cur = conn.cursor()

################ LISTS ################
@app.route('/list', methods=['GET', 'POST'])
def index_list():
    if request.method == 'GET':
        cur.execute("""SELECT * FROM lists""")
        res_dict = cur.fetchall()
        return json.dumps(res_dict)
    elif request.method == 'POST':
        budget = request.form["budget"]
        if ',' in request.form["budget"]:
            budget = budget.replace(',', '.')
        cur.execute("""
            INSERT INTO lists (name, budget, created_at)
            VALUES (%(name)s, %(budget)s, %(created_at)s);
            """,
            {'name': request.form["name"], 'budget': budget, 'created_at': str(time.strftime("%Y-%m-%d"))})
        conn.commit()
        return 'Your list has been successfully saved !'

@app.route('/list/<int:list_id>', methods=["GET", "DELETE"])
def show_list(list_id):
    if request.method == 'GET':
        cur.execute("""SELECT * FROM lists WHERE id=""" + str(list_id))
        res_dict = cur.fetchall()
        return json.dumps(res_dict)
    elif request.method == 'DELETE':
        cur.execute("""
            DELETE FROM lists WHERE id=%(id)s
            """, {'id': list_id})
        cur.execute("""
            DELETE FROM items WHERE list_id=%(list_id)s
            """, {'list_id': list_id})
        conn.commit()
        return 'Your list has been successfully deleted'


################ ITEMS ################

@app.route('/list/<int:list_id>/item', methods=["GET", "POST"])
def index_item(list_id):
    if request.method == 'GET':
        cur.execute("""SELECT * FROM items WHERE list_id=%(list_id)s""",
            {'list_id': list_id})
        res = cur.fetchall()
        return json.dumps(res)
    if request.method == 'POST':
        now = str(time.strftime("%Y-%m-%d"))
        cost = request.form["cost"]
        if ',' in cost:
            cost = cost.replace(',', '.')
        cur.execute("""
            INSERT INTO items (name, cost, link, image_link, created_at, list_id)
            VALUES (%(name)s, %(cost)s, %(link)s , %(image_link)s, %(created_at)s, %(list_id)s);
            """,
            {
                'name': request.form["name"],
                'cost': cost,
                'link': request.form["link"],
                'image_link': request.form["image_link"],
                'created_at': now,
                'list_id': list_id
            })
        conn.commit()
        return "You've adde a new item in your list"

@app.route('/list/<int:list_id>/item/<int:item_id>', methods= ["GET", "DELETE"])
def show_item(list_id, item_id):
    if request.method == "GET":
        cur.execute("""SELECT * FROM items WHERE list_id=%(list_id)s AND id=%(id)s""",
            {'list_id': list_id, 'id': item_id})
        res = cur.fetchall()
        return json.dumps(res)
    elif request.method == "DELETE":
        return 'bhjiok'
