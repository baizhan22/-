import os
import yaml

class YamlUtil:
    def read_extract_yaml(self,key):
        """读取yaml文件并且提取变量数据"""
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/extract.yaml',mode='r',encoding='utf-8') as f:
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]

    def write_extract_yaml(self,data):
        """把获取到的数据写入yaml文件"""
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/extract.yaml', mode='a', encoding='utf-8') as f:
            value = yaml.dump(data=data,stream=f,allow_unicode=True)

    def clear_extract_yaml(self):
        """清空yaml文件内所有数据"""
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/extract.yaml', mode='w', encoding='utf-8') as f:
            f.truncate()

    def read_testcase_yaml(self, yaml_name):
        """读取测试用例的yaml文件"""
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ '/testcase/'+yaml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value