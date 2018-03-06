#coding=utf-8

import thread
import time

def fun1():
    print 'Hello World %s'%time.ctime()

def main():
    thread.start_new_thread(fun1,( ))
    thread.start_new_thread(fun1,( ))
    time.sleep(2)
if __name__ == '__main__':
    main()
    
    
    
    by python 2.7
