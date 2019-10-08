import pika

from rabbitmq_template import RabbitmqTemplate


class RabbitmqRcv(RabbitmqTemplate):

    def __init__(self):
        super(RabbitmqRcv, self).__init__()

    # 消息处理函数，执行完成才说明接收完成，此时才可以接收下一条，串行
    def dongcallbackfun(self, v1, v2, v3, bodyx):
        # print("得到的数据为:", bodyx)
        pass

    def rcv(self):
        # 接收准备
        self.channelx.basic_consume(self.queuename,  # 队列名
                                    self.dongcallbackfun,  # 收到消息的回调函数
                                    True)  # 是否发送消息确认
        print("-------- 开始接收数据 -----------")

        # 开始接收消息
        self.channelx.start_consuming()


# RabbitmqRcv().rcv()
