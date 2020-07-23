$(function() {

    var url = window.location.href;
    var arry = url.split('/');
    var product_id = arry[arry.length - 1];

    get_product();

    function get_product() {
        $.ajax({
            url:$SCRIPT_ROOT+'/api/wechat/product',
            type:"GET",
            contentType: "application/json; charset=utf-8",
            data:{'id':product_id},
            dataType:'json',
            success:function(data){
                show_imgs(data.data.product.product_imgs);
            },
            error:function(data){
                console.log(data.responseJSON.msg);
            }
        })
    }

    function show_imgs(data) {
        var imgs = '';
        data.map(function(re,i){
            var src = re.url
            return imgs+="<img class='product_img' src='"+src+"''></img>";
        })
        $('.img-wrap').html(imgs);
    }

});