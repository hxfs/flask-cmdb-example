$(document).ready(function(){
    $("#login-form").click(function(){
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
                }
            });
        }
        else
        {
            alert("请填写用户名或密码!")
        }
    });
});