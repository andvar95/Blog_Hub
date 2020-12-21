
var entro = 0;
function verpass(){
    console.log("entro")
    if (entro == 0) {
    
        document.getElementById('clave1').type = "text";
        document.getElementById('clave2').type = "text";
        entro = 1;
    } else {
        document.getElementById('clave1').type = "password";
        document.getElementById('clave2').type = "password";
        entro = 0;

    }


};