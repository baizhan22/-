import time
import random
from common.yaml_util import YamlUtil

class Public(YamlUtil):
    def times(self):
        #获取当前时间
        time.time()

    def rdm(self):
        w=random.randint(1,30)
        return int(200)