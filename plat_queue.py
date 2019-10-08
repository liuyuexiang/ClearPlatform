from multiprocessing import Queue, Process


def write(q):
    for i in ['a', 'b', 'c', 'd']:
        q.put(i)
        print('put {0} to queue'.format(i))


def read(q):
    while 1:
        result = q.get()
        print("get {0} from queue".format(result))


def main():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()  # 停止
    # 相当于join，等pr完成以后，当whlie没有任何执行后，结束。


if __name__ == '__main__':
    main()
