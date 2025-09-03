import pytest

from config.config import SQL1, SQL2
from utils.http_requests import jdbc_op_requests


@pytest.fixture(scope='session', autouse=True)
def delete_data():
    yield

    sqls = [SQL1, SQL2]
    jdbc_op_requests(sqls)

