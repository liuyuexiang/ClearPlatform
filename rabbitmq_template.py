import pika

from yml_config import SysConfig


class RabbitmqTemplate(SysConfig):
    def __init__(self):
        super(RabbitmqTemplate, self).__init__()
        queuename = self.config['queue']['queuename']
        username = self.config['queue']['username']
        password = self.config['queue']['password']
        host = self.config['queue']['host']
        port = self.config['queue']['port']

        # 管道名称
        self.queuename = queuename
        # 建立连接
        userx = pika.PlainCredentials(username, password)
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', credentials=userx))
        # 开辟管道
        self.channelx = self.conn.channel()

        # 声明队列，参数为队列名
        self.channelx.queue_declare(queue=self.queuename, durable=True)

    def send(self, msg):
        pass

    def rcv(self):
        pass


# RabbitmqTemplate()

