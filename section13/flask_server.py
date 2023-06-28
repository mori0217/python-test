import sqlite3

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)


@app.route('/')
def index():
    return "index page"


@app.route('/hello')
@app.route('/hello/<username>')
def hello(username=None):
    # return "hello world {}".format(username)
    return render_template('hello.html', username=username)


@app.route("/post", methods=['POST', "PUT", "DELETE"])
def show_post():
    return str(request.values["key1"])


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("chapter13.db")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/employee", methods=["POST", "PUT", "DELETE"])
@app.route("/employee/<name>", methods=["GET"])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)")
    db.commit()

    name = request.values.get("name", name)
    if request.method == "GET":
        curs.execute("SELECT * FROM employee WHERE name=?", (name,))
        employee = curs.fetchone()
        if not employee:
            return "No", 404
        user_id, name = employee
        return "{}, {}".format(user_id, name), 200
    elif request.method == "POST":
        curs.execute("INSERT INTO employee(name) VALUES(?)", (name,))
        db.commit()
        return "created {}".format(name), 201
    elif request.method == "PUT":
        new_name = request.values["new_name"]
        curs.execute("UPDATE employee SET name=? WHERE name=?", (new_name, name))
        db.commit()
        return "updated {}: {}".format(name, new_name), 200
    elif request.method == "DELETE":
        curs.execute("DELETE FROM employee WHERE name=?", (name,))
        db.commit()
        return "deleted {}".format(name), 200
    curs.close()


def main():
    app.debug = True
    # app.run(host='127.0.0.1', port=5000)
    app.run()


if __name__ == '__main__':
    main()
