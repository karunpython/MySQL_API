from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


def get_connection():
    conn = mysql.connector.connect(host="localhost", user="root", password="", db="winds")
    return conn


@app.route('/')
def get_all_data():
    global rows
    conn = get_connection()
    cur = conn.cursor()
    query = "select * from student"
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    output = []
    for i in rows:
        output.append({
            'id': i[0],
            'name': i[1],
            'mobile': i[2],
            'password': i[3],
        })

    return jsonify({'status': True, 'result': output})


def get_one(mob):
    global rows
    conn = get_connection()
    cur = conn.cursor()
    query = "select * from student where mobile='" + mob + "'"
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    output = []
    for i in rows:
        output.append({
            'id': i[0],
            'name': i[1],
            'mobile': i[2],
            'password': i[3],
        })

    return output


@app.route('/signup', methods=['POST'])
def sign_up():
    payload = request.get_json()
    name = payload['name']
    mob = payload['mobile']
    pas = payload['password']

    conn = get_connection()
    cur = conn.cursor()
    query = "insert into student(name,mobile,password) values(%s,%s,%s)"
    args = (name, mob, pas)
    cur.execute(query, args)
    conn.commit()
    conn.close()
    return jsonify({'status': True, 'message': 'you have been successfully signup'})


@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    mob = payload['mobile']
    pas = payload['password']

    conn = get_connection()
    cur = conn.cursor()
    query = "select mobile,password from student where mobile='" + mob + "' AND password='" + pas + "'"
    cur.execute(query)
    if cur.fetchone() is not None:
        s = cur.fetchone()
        conn.commit()
        conn.close()
        return jsonify({'status': True, 'message': 'successfully login','result':get_one(mob)})
    else:
        return jsonify({'status': False, 'message': 'Invalid username or password'})


if __name__ == '__main__':
    app.run(debug=True)
