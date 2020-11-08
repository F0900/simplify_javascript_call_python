初衷：简化前后端调用环节减少代码量，使其前后端调用似普通方法调用。支持调用过程运行中后端返回数据至前端（后端使用：send('数据')）。

使用说明：

后端：

重命名POC脚本，在原脚本名前添加load_（以load_开头的文件将被加载待用），将脚本归档至load文件夹内。

需要在原POC脚本内，添加如下代码：

# class 类名需为：Regist

class Regist(object):

# 注册函数，前端调用后端的名称

def onRegist(self):

return '前端调用名'

# 将原POC脚本入口函数添加到run函数内

# 参数：send -> 内联函数（使用：send(data)）

# 参数：data -> 前端传的数据

def run(self,send,data):

print(status)

send('脚本运行中返回给前端的数据')

print(data)

return '后端返回数据'

前端：

1、自定义html代码

将内容块的html代码块存到单独一个文件夹，如：readme.html。将该html文件存放至static/page内（如：static/page/readme.html）

在load.js内添加以下代码：regist("page/readme.html")

2、自定义菜单（自定义的html代码，如何待用？）

在自定义html文件内添加如下代码：

<script>

menu_onload('工具说明',"内容div id")

</script>

<div id="内容div id" class="content">

html代码

</div>

其中：menu_onload('菜单名称',"tool_explain_content")

前端调用：

call('后端脚本onRegist函数内return 返回值', 传给脚本的数据)

示例：

在load文件夹内添加load_example.py脚本文件

内容为：

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

在static文件夹内添加html_example.html页面文件

内容为：

<script>

menu_onload('菜单实例',"html_example")

</script>

<div id="html_example" class="content">

<button onclick="ex()">a</button>

</div>

<script>

function example(data){

alert('example')

alert(data)

}

function ex(){

call('server_example', 'data example', 'example')

}

</script>

将html_example.html路径注册到static/load.js内

regist("page/html_example.html")
