import logging
import jsonpath
from utils.http_requests import jdbc_select_requests


# HTTP响应断言
def http_assert(requests_data, res):
    if requests_data['check']:
        json_actual = jsonpath.jsonpath(res.json(), expr=requests_data['check'])[0]
        logging.info('HTTP响应结果:{}'.format(res.json()))
        logging.info('HTTP响应预期结果:({}) == 实际结果:({})'.format(requests_data['expect'], json_actual))
        assert requests_data['expect'] == json_actual
    else:
        logging.info('HTTP响应结果:{}'.format(res.json()))
        logging.info('HTTP响应:({}) in 实际结果:({})'.format(requests_data['expect'], res.text))
        assert requests_data['expect'] in res.text


# 数据库响应断言
def sql_assert(requests_data):
    if requests_data['sql_expect']:
        sql = requests_data["sql_check"]
        sql_actual = jdbc_select_requests(sql)
        logging.info('数据库预期结果:({}) == 实际结果:({})'.format(requests_data['sql_expect'], sql_actual))
        assert requests_data['sql_expect'] == sql_actual

