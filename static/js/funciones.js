var entro = 0;

function ver() {
    
    if (entro == 0) {
        document.getElementById('Seccion_sesion').style.visibility = "visible";
        entro = 1;
    } else {
        document.getElementById('Seccion_sesion').style.visibility= "hidden";
        entro = 0;

    }

};

