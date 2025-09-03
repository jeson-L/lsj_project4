import os
import pytest

if __name__ == '__main__':
    pytest.main(['-v', './testcases/testcase.py', '--alluredir', './report/report_json', '--clean-alluredir'])
    os.system('allure generate ./report/report_json -o ./report/html_report --clean')
