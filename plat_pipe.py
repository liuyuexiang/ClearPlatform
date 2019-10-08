import time
from multiprocessing import Pipe, Process


def proc1(pipe, msg):
    pipe.send(msg)
    print("send {0} to pipe".format(msg))
    time.sleep(1)


def proc2(pipe):
    while 1:
        result = pipe.recv()
        print("recv {0} from pipe".format(result))
        time.sleep(1)


def main():
    pipe = Pipe(duplex=False)
    print(type(pipe))
    p1 = Process(target=proc1, args=(pipe[1], "hello"))
    p2 = Process(target=proc2, args=(pipe[0],))  # 接收写0
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    time.sleep(11)
    proc1(pipe[1],"yes")
    # pipe[0].close()
    # pipe[1].close()


if __name__ == '__main__':
    main()
