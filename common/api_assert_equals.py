# -*- coding: utf-8 -*-

class Equals:

    def wh(self,Expected_result,actual_result,assert_result,error=None):
        resluts = []
        whh_result={
            "Expected_result":Expected_result,
            'actual_result':actual_result,
            'assert_result':assert_result
        }

        resluts.append(whh_result)
        return resluts

    def status_code(self,kwargs):
        try:
            assert kwargs[0].status_code==int(kwargs[1])
            resluts=self.wh(Expected_result=kwargs[1],actual_result=kwargs[0].status_code,assert_result=True)
        except AssertionError as e:
            resluts=self.wh(Expected_result=kwargs[1], actual_result=kwargs[0].status_code, assert_result=False)
        return resluts

    def whh(self,kwargs):
        try:
            assert kwargs[0].elapsed.total_seconds() <= kwargs[1]
            resluts = self.wh(Expected_result=kwargs[1], actual_result=f"响应时间{kwargs[0].elapsed.total_seconds()}小于{kwargs[1]}", assert_result=True)
        except AssertionError as e:
            resluts = self.wh(Expected_result=kwargs[1], actual_result=f"响应时间{kwargs[0].elapsed.total_seconds()}大于于{kwargs[1]}", assert_result=False)
        return resluts
