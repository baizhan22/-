import pytest
from common.yaml_util import YamlUtil
from common.api_util import RequestUtil
from common.yaml_hotloading import Hot_Loading
import os
# -*- coding: utf-8 -*-

class Test_api:
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('login.yaml'))
    def test_1(self,caseinfo):
        RequestUtil().gjz(**caseinfo)




if __name__ == '__main__':
    pytest.main(['-vs','test_login.py'])