import logging

from rabbitmq_rcv import RabbitmqRcv


class SoketClient(RabbitmqRcv):
    def dongcallbackfun(self, v1, v2, v3, bodyx):
        logging.info("接收到消息为：%s" % bodyx)
        print("得到的数据为:%s" % bodyx)
        print(self.config['socket']['client']['port'])


SoketClient().rcv()
