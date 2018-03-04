$(document).ready(function(){
    $("#sidebar-menu ul li").click(function(){
        if($(this).children(".box-drawer").is(":hidden")){
            if(!$(this).children(".box-drawer").is(":animated")){
                $(this).children(".box-drawer").animate({
                    height: 'show'
                }, 1000)
            .end().siblings().find(".box-drawer").hide(1000);
            }
        } else{
            if(!$(this).children(".box-drawer").is(":animated")){
                $(this).children(".box-drawer").animate({
                    height: 'hide'
                }, 1000)
                end().siblings().find(".box-drawer").hide(1000);
            }
        }
    })
})