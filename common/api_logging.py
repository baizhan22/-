import json
import logging
import sys
import colorlog
log_color_config={
    'DEBUG':'white',
    'INFO':'green',
    'WARNING':'yellow',
    'ERROR':'red',
    'CRITICAL':'bold_red'
}
# ft=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s  %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s',log_colors=log_color_config)


class Logging:
    def init_logger(self,logger_name='mylogger',logname=None):
        logger=logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            if logname==None:
                logger.addHandler(self.init_fileHd())
                logger.addHandler(self.init_streamHd())
            else:
                logger.addHandler(self.init_fileHd(filename=logname))
                logger.addHandler(self.init_streamHd())
        return logger

    def init_streamHd(self):
        streamHandler=logging.StreamHandler()
        streamHandler.setLevel(logging.INFO)
        streamHandler.setFormatter(formatter)
        return streamHandler

    def init_fileHd(self,filename='logging.log'):
        fileHandler=logging.FileHandler(filename=filename)
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(formatter)
        return fileHandler

    def log_INFO(self,**kwargs):
        self.init_logger().info('开始执行第{}条用例'.format(kwargs['id']))
        self.init_logger().info('接口名称:{}'.format(kwargs['api_name']))
        self.init_logger().info('请求方式:{}' .format(kwargs['request']['method']))
        self.init_logger().info('请求地址:{}' .format(kwargs['request']['url']))
        if kwargs['request']['method']=='post':
            self.init_logger().info('请求参数:{}' .format(kwargs['request']['data']))
        else:
            self.init_logger().info('请求参数:{}' .format(kwargs['request']['params']))

    def log_aserrt_result(self,Expected_result,actual_result,assert_result):
        self.init_logger().info('预期结果:{}'.format(Expected_result))
        self.init_logger().info('实际结果:{}'.format(actual_result))
        if assert_result == True:
            self.init_logger().info('断言结果:{}'.format('成功'))
        else:
            self.init_logger().error('断言结果:{}'.format('失败'))
    def log_error(self,d):
        self.init_logger().error('{}'.format(d))