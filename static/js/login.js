$(document).ready(function(){
    console.log("I am JQuery")
    $("#login-form").submit(function(e){
        e.preventDefault();
        var username = $(".username").val();
        var password = $(".password").val();
        if (username.replace(/(^\s*)|(\s*$)/g, "").length != 0 && password.replace(/(^\s*)|(\s*$)/g, "").length != 0 ){
            $.post(
                'http://localhost:5000/login',
                {username:username,password:password},
                function(data) {
                    console.log(data)
                }); 
        }
        else
        {
            alert("请填写用户名或密码!")
        }
    });
});