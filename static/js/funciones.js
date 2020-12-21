var entro = 0;

function ver() {
    console.log("entro");
    if (entro == 0) {
        document.getElementById('Seccion_sesion').style.visibility = "visible";
        entro = 1;
    } else {
        document.getElementById('Seccion_sesion').style.visibility= "hidden";
        entro = 0;

    }

};

