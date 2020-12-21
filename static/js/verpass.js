
var entro = 0;
function verpass(){
    console.log("entro")
    if (entro == 0) {
        document.getElementById('clave').type = "text";
        entro = 1;
    } else {
        document.getElementById('clave').type = "password";
        entro = 0;

    }


};