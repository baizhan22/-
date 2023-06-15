
# -*- coding: utf-8 -*-

class Contains:
    def wh(self, Expected_result, actual_result, assert_result, error=None):

        resluts = []
        whh_result = {
            "Expected_result": Expected_result,
            'actual_result': actual_result,
            'assert_result': assert_result
        }
        resluts.append(whh_result)
        return resluts

    def text1(self,kwargs):
        try:
            assert kwargs[1] in kwargs[0].text
            resluts=self.wh(Expected_result=kwargs[1],actual_result='在返回结果中查询到了:{}'.format(kwargs[1]),assert_result=True)
        except AssertionError as e:
            resluts=self.wh(Expected_result=kwargs[1], actual_result='在返回结果中没有查询到:{}'.format(kwargs[1]), assert_result=False)
        return resluts


    def text2(self,kwargs):
        resluts=[]
        for i in kwargs[1]:
            for key,value in i.items():
                try:
                    assert str(value) in kwargs[0].text
                    reslut=self.wh(Expected_result=value,actual_result='在返回结果中查询到了:{}'.format(value),assert_result=True)
                    resluts.append(reslut)
                except AssertionError as e:
                    reslut=self.wh(Expected_result=value, actual_result='在返回结果中没有查询到:{}'.format(value), assert_result=False)
                    resluts.append(reslut)
        return resluts

