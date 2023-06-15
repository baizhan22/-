from common.api_assert_equals import Equals
from common.api_assert_contains import Contains
from common.api_logging import Logging
import pytest



class Asserts():
    def __init__(self):
        self.log=Logging()
    def method_assert(self,respons,asserts):
        result=[]
        for i in asserts:
            for key,value in i.items():
                p=[respons,value]
                assert_result=getattr(Asserts(),key)(p)
                for s in assert_result:
                    assert_result=s[0]
                    result.append(assert_result)

        return result



    def asserts_preprocess(self,respons,asserts):
        w=self.method_assert(respons,asserts)
        assert_result=[]
        for i in w:
            if True==i.get('assert_result'):
                self.log.log_aserrt_result(i.get('Expected_result'), i.get('actual_result'), i.get('assert_result'))
            else:
                assert_result.append(i.get('assert_result'))
                self.log.log_aserrt_result(i.get('Expected_result'), i.get('actual_result'), i.get('assert_result'))
        try:
            assert  False not in assert_result
        except:
            raise

    def equals(self,kwargs):
        eq=Equals()
        result=[]
        for key,value in kwargs[1].items():
            p=[kwargs[0],value]
            equals_result=getattr(eq,key)(p)
            result.append(equals_result)
        return result



    def contains(self,kwargs):
        eq = Contains()
        result = []
        for key, value in kwargs[1].items():
            p = [kwargs[0], value]
            equals_result = getattr(eq, key)(p)
            result.append(equals_result)
        if 'text2' in kwargs[1].keys():
            return result[0]
        else:
            return result

