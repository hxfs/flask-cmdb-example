$(document).ready(function(){
    $("#submit").click(function(){
        console.log("I am JQuery")
        var username = $(".username").val();
        var password = $(".password").val();
        if (username.replace(/(^\s*)|(\s*$)/g, "").length != 0 && password.replace(/(^\s*)|(\s*$)/g, "").length != 0 ){
            var formjson = {"username": username, "password": password};
            $.ajax({
                type: 'POST',
                url: 'http://localhost:5000/login',
                data: formjson,
                success: function(data){
                    console.log(data)
                    var rdata = jQuery.parseJSON(data);
                    if (rdata.data.status == 'success'){
                        window.location.replace("http://localhost:5000/index");
                    }
                    else{
                        alert("用户名或密码错误")
                    }
                }
            });
        }
        else
        {
            alert("请填写用户名或密码!")
        }
    });
});