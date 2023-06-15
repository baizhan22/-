from common.yaml_util import YamlUtil
import requests as  rs
# -*- coding: utf-8 -*-
from common.api_logging import Logging
from common.api_assert import Asserts
from common.yaml_hotloading import Hot_Loading
class RequestUtil(YamlUtil):
    def __init__(self):
        self.session=rs.Session()
        self.log=Logging()
        self.asserts=Asserts()

    def request_method(self, **kwargs):
        rq = kwargs['request']
        asserts = kwargs['assert']
        self.log.log_INFO(**kwargs)
        respons = self.session.request(**rq)
        w=Hot_Loading().jsonpth_config(respons=respons,**kwargs)
        if w !=None:
            self.log.init_logger().info('参数提取完成')
        self.asserts.asserts_preprocess(respons,asserts)

    #检测yaml文件格式
    def gjz(self,**kwargs):
        if 'request' in kwargs.keys() and 'assert' in kwargs.keys() and 'api_name' in kwargs.keys():
            rq = kwargs['request']
            if 'url' in rq.keys() and 'method' in rq.keys():
                self.log.init_logger().info('YAML文件格式检测通过')
                kwargs=Hot_Loading().loading_ccnfig(**kwargs)
                self.log.init_logger().info('YAML文件热加载完成')
                self.request_method(**kwargs)
            else:
                self.log.log_error('POST请求的二级关键字必须包含:url,data')
                assert 1==2
        else:
            self.log.log_error('一级关键字必须包换:name,request,assert')
            assert 1 == 2