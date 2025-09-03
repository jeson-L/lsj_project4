import logging

import pymysql
import requests

from config.config import DATABASE_IP, DATABASE_PORT, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD


# HTTP请求
def http_requests(request_data):
    logging.info(request_data)
    return requests.request(**request_data)


# jdbc查询请求
def jdbc_select_requests(sql):
    conn = pymysql.connect(
        host=DATABASE_IP,
        port=DATABASE_PORT,
        database=DATABASE_NAME,
        charset="utf8",
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchone()[0]
    cur.close()
    conn.close()
    return data


# jdbc增删改请求
def jdbc_op_requests(sqls):
    conn = pymysql.connect(
        host=DATABASE_IP,
        port=DATABASE_PORT,
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )
    cur = conn.cursor()
    for i in sqls:
        cur.execute(i)
    conn.commit()
    cur.close()
    conn.close()
