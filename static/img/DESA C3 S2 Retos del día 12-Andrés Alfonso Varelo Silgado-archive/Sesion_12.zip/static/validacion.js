var intentos = 3;
var pss = document.getElementById('password');



function mostrar() {
  pss.type = 'text';

  }
function no_mostrar(){
  pss.type = 'password';
  console.log("sali");
}

function validar_formulario() {
     
    var usuario = document.getElementsByName('usuario')[0];
    var password = document.getElementsByName('password')[0];
    var boton = document.getElementsByClassName('boton')[0];
    
    if (document.getElementsByName('usuario').value == "Andres" && document.getElementsByName('usuario').value == "1234" ){

        alert("Ingreso exitoso");
    }

    else{
        intentos--;
        alert("Intentos faltantes "+intentos);
    }

    if(intentos==0){
        usuario.disabled = true;
        password.disabled = true;
        boton.disabled = true;

    }
          };
        



    
