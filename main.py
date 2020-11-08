#-*- coding:utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import copy
import  sqlite3
import load
import sys
import time


from flask import Flask, request, render_template
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import gevent


def router(user_socket,data):
    if(data):
        json_data = json.loads(data)
        if 'name' in json_data and 'data' in json_data:
            name = json_data['name']
            if name in load_classes:
                def send(message):
                    if user_socket:
                        user_socket.send( json.dumps( {'name': name, 'data':message } ))
                result = (load_classes[name].run(send,json_data['data']))
                user_socket.send( json.dumps( {'name': name, 'data':result } ))
            else:
                user_socket.send(json.dumps({"msg": "check name"}))
        else:
            user_socket.send(json.dumps({"msg": "json data key must name and data"}))


app = Flask(__name__, static_url_path='')


@app.route('/')
def web():
    return render_template('index.html')

@app.route('/ws')
def index():
    user_socket = request.environ.get("wsgi.websocket") 
    try:
        while True:
            msg = user_socket.receive()
            gevent.spawn(router,user_socket,msg)

    except  Exception as e:
        print(e)
        return 'Finished'

if __name__ == '__main__': 
    path = 'load'
    sys.path.append(path)
    load_classes = load.on_load()
    http_server = WSGIServer(('0.0.0.0',8010), app, handler_class=WebSocketHandler) 
    http_server.serve_forever()



    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        