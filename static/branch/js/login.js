$("#loginForm").validate({
    rules:{
        email:{
            required:true,
            email:true,
        },
        password:{
            required:true
        },
        messages:{
            email:{
                required:"This field is required",            
            },
            password:{
                required:"This field is required"
            }
        }
    },
    submitHandler: function (e){
        var email = $('input[name=email]').val();
        var password = $('input[name=password]').val();      
        var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
        data = {
            'email':email,
            'password':password,
            csrfmiddlewaretoken:csrftoken
        } 
        $.ajax({
            url:"/branchapi/login/",
            type: "POST",
            data: data,
            statusCode: {
                400: function() {
                    $("#errorForm").html("Invalid username or password")
                },
                200:function(response){
                    localStorage.setItem("token",response['token']);
                    window.location="/branch/dashboard/"
                }
            },
        });
    } 
});

$("#email").keyup(function(){
    $("#errorForm").html('')
})