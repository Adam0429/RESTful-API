#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
import MySQLdb
app = Flask(__name__)

mysql_host = "mysql"
mysql_user = "root"
mysql_pwd = "970429"
mysql_db_name = "demo"

"""
CREATE DATABASE `demo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `demo`.`user_info` (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`name` varchar(200) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

def query_db(sql):
    db = MySQLdb.connect(mysql_host, mysql_user, mysql_pwd, mysql_db_name)
    cur = db.cursor()
    try:
        cur.execute(sql)
        result = cur.fetchall()
    except:
        print("error: sql:" + sql)
    cur.close()
    db.close()
    return result

def update_db(sql):
    print(sql)
    db = MySQLdb.connect(mysql_host, mysql_user, mysql_pwd, mysql_db_name)
    cur = db.cursor()
    try:
        cur.execute(sql)
    except:
        print("error: sql:" + sql)
    db.commit()
    cur.close()
    db.close()


@app.route("/list")
def list():
    results = query_db(" select id,name from `demo`.`user_info` ")
    out = "results:\n"
    for result in results:
        id = result[0]
        name = result[1]
        out += "id:" + str(id) + ",name:" + name +"\n"
    return out

@app.route("/add")
def add():
    sql = " insert ignore into `demo`.`user_info`(`name` ) values ('zhangsan') "
    update_db(sql)
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)