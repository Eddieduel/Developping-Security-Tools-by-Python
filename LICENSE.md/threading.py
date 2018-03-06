#coding=utf-8

import threading
import time

def fun1(key):
    print 'hello %s: %s \n'%(key,time.ctime())

def main():
    threads = []
    keys = ['BIN','JACK','ROOK']

    threads_count = len(keys)

    for i in range(threads_count):
        t = threading.Thread(target=fun1,args=(keys[i],))
        threads.append(t)
    for i in range(threads_count):
        threads[i].start()
    for i in range(threads_count):
        threads[i].join()

if __name__ == '__main__':
    main()
