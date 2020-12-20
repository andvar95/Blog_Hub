$(document).ready(function(){
console.log("hola")


function comentar(){
    console.log("entre")
    console.log($("#formComent").serializeArray())
    req = $.ajax({
        url:'/comentario',
        data: $("#formComent").serializeArray(),
        type: 'POST',
        success: function(response) {
            console.log(response);
            
        },
        error: function(xhr) {
            console.log(xhr);
        }
       
    });

    req.done(function(){
        console.log("update")

    });
    }



$("#formComent").submit(function(event){
    event.preventDefault();
    comentar();
    console.log("comente")
});

});