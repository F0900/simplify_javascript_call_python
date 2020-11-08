#-*- coding:utf-8 -*-

def poc(data):
    print("poc")
    print(data)
    return 'return server poc'

class Regist(object):
    def onRegist(self):
        return 'server_example'
    def run(self,send,data):
        send(1)
        send(2)
        p = poc(data)
        send(p)
        send(3)
        print(data)
        return 'return server example'


