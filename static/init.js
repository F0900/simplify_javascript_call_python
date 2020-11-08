
// 所有内容ID
var all_content_ids = []

var uuid1 = function () {
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "";

    var uuid = s.join("");
    return uuid;
}
// 菜单对应加载的内容取ID
var menu_onload = function(menu_name,  content_id){
    var uuid = uuid1()
    var html = '<div class="menu">    <p id="'+uuid+'">'+menu_name+'</p></div>'
    $("#menus").append(html)

    all_content_ids.push(content_id)
    $("#"+uuid).click(function(){

        var display = $("#"+content_id).css('display')
        if(display == 'none'){
            for(var i =0; i < all_content_ids.length;  i++){
                $("#"+all_content_ids[i]).css('display','none')
            }
            $("#"+content_id).css('display',"block")
        }else{
            $("#"+content_id).css('display','none')
        }
    })
}

var regist = function(page_path){
    $("#content").append("<div id = '"+page_path.replace("/","").replace(".","")+"'></div>")
    // console.log((page_path.replace("/","")))
    $("#"+(page_path.replace("/","").replace(".","")) ).load(page_path);
}
