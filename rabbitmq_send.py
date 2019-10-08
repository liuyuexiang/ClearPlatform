import pika

from rabbitmq_template import RabbitmqTemplate


class RabbitmqSend(RabbitmqTemplate):
    def __int__(self):
        super(RabbitmqTemplate, self).__init__()

    def send(self, msg=""):
        # 发送数据，发送一条，如果要发送多条则复制此段
        self.channelx.basic_publish(exchange="",
                                    routing_key=self.queuename,  # 队列名
                                    body=msg,  # 发送的数据
                                    properties=pika.BasicProperties(
                                        delivery_mode=2,  # 实现消息永久保存
                                    )
                                    )
        print("--------发送数据完成-----------")

        # 关闭连接
        self.conn.close()
