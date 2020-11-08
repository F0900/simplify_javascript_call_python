

var ws = new WebSocket("ws://127.0.0.1:8010/ws");
// 发送
function send(name,data){
    ws.send(JSON.stringify({"name":name, 'data':data}))
}
//根据方法名调用方法
function callModelFun(functionName,data){
    //根据函数名得到函数类型
    var  func=eval(functionName);
    //创建函数对象，并调用
    new func(data);
}

regsit_map = {}
// 接收
ws.onmessage = function(event) {
    json_data = JSON.parse(event.data)
    if (json_data['name'] in regsit_map){
        callModelFun(regsit_map[json_data['name']],json_data['data'])
    }else{
        callModelFun(json_data['name'],json_data['data'])
    }
};
// 后端注册名，json参数，前端调用函数名（不传为后端注册名）
var call = function(back_regist,data,fun_name){
    if(fun_name){
        regsit_map[back_regist] = fun_name
    }
    send(back_regist,data)
}
