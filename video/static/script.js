$('document').ready(function(){
    $('div.cm-s-mdn-like').on('click',function () {
        var id = $(this).attr('id')
        $.ajax({
            url:"/add_like/",
            data:{"id":id},
            success:function (data) {
                $("h3#like" + id).html("this video has " +data+ " Likes")
            }
        });
    })
});