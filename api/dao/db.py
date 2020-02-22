import os
import json
import pymysql

init_table_sql = """CREATE TABLE IF NOT EXISTS friend (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    age INT(11) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    hobby VARCHAR(255) NOT NULL,
    remark VARCHAR(255) NOT NULL,
    status INT(11) DEFAULT 1,
    create_time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    update_time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);"""


def get_connection():
    return pymysql.connect(host='mysql', port=3306, user='root', password=os.environ.get('MYSQL_PASSWORD'),
                           db=os.environ.get('MYSQL_DATABASE'), charset='utf8')


def execute_sql(execute_type, sql=None, params=None):
    db = get_connection()
    try:
        if execute_type == 1:
            # C U D
            with db.cursor() as cursor:
                rows = cursor.execute(sql, params)
            db.commit()
            return rows
        elif execute_type == 2:
            # R
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, params)
                return cursor.fetchall()
    except Exception as e:
        print('Reason :', e)
        db.rollback()
    finally:
        db.close()


def init_db():
    db = get_connection()
    try:
        with db.cursor() as cursor:
            cursor.execute(init_table_sql)
        db.commit()
    except Exception as e:
        print(e)


def get_friend(name):
    get_friend_sql = "SELECT id, name, age, gender, hobby, remark FROM friend WHERE name = %s AND status = 1"
    t = (name)
    return json.dumps({'results': execute_sql(2, get_friend_sql, t)})


def get_friend_list():
    get_friend_list_sql = "SELECT id, name, age, gender, hobby, remark FROM friend WHERE status = 1"
    return json.dumps({'results': execute_sql(2, get_friend_list_sql)})


def post_friend(params):
    insert_friend_sql = 'INSERT INTO friend (name, age, gender, hobby, remark) VALUES (%s, %s, %s, %s, %s)'
    t = (params['name'], params['age'], params['gender'], params['hobby'], params['remark'])
    return json.dumps({'result': execute_sql(1, insert_friend_sql, t)})


def put_friend(friend_id, params):
    put_friend_sql = """UPDATE friend SET name = %s, age = %s,
                        gender = %s, hobby = %s, remark = %s 
                        WHERE id = %s"""
    t = (params['name'], params['age'], params['gender'], params['hobby'], params['remark'], friend_id)
    return json.dumps({'result': execute_sql(1, put_friend_sql, t)})


def del_friend(friend_id):
    del_friend_sql = "UPDATE friend SET status = 0 WHERE id = %s"
    t = (friend_id)
    return json.dumps({'result': execute_sql(1, del_friend_sql, t)})
