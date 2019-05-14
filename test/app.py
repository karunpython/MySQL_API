import mysql.connector


def getConnection():
    conn = mysql.connector.connect(host="localhost", user="root", password="", db="winds")
    return conn


def insert_student(name,mobile,password):
    conn = getConnection()
    cur = conn.cursor()
    query = "insert into student(name,mobile,password) values(%s,%s,%s)"
    args=(name,mobile,password)
    cur.execute(query,args)
    conn.commit()
    conn.close()
    print('Data inserted..')

#
# def get_all_student():
#     conn = getConnection()
#     cur = conn.cursor()
#     query = "select * from student"
#     cur.execute(query)
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     return rows

def get_one_student():
    conn = getConnection()
    cur = conn.cursor()
    query = "select * from student where id=1"
    cur.execute(query)
    rows=cur.fetchone()
    conn.commit()
    conn.close()
    return rows

def main():
    print(get_one_student())

if __name__ == '__main__':
    main()
