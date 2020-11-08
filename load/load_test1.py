#-*- coding:utf-8 -*-


status = 0

class Regist(object):
    def onRegist(self):
        return 'wolaizhuce'
    def run(self,send,data):
        global status
        print(status)
        
        status = 1
        print(status)
        send(1)
        send(2)
        send(3)
        print(data)
        return 'test'


