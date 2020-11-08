#-*- coding:utf-8 -*-
import os,sys

#这里放着你要操作的文件夹名称
path = 'load'
 

#添加被动态加载的路径
sys.path.append(path)

files = os.listdir(path)

#动态加载py
def on_load():
    load_module = []
    for load_file in files:
        loaf_file_name = str(load_file).split('.')[0]
        if loaf_file_name.find('load_') == 0:
            module =__import__(loaf_file_name) 
            load_module.append(module)
    classes = {}
    for module in load_module:
        _class = getattr(module,'Regist')()  
        
        classes[_class.onRegist()] = _class

    return classes
    
