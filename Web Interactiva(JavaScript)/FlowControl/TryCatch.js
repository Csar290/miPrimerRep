try {
    //Error
    asasfgdd
    /*throw {
        error: "Nombre del error",
        info: "Informacion del error"
    }*/
} catch (e/*.error*/) {
    //Control de el error
    console.log("Ha ocurrido un error")
    //Condiciones
} finally {
    console.log("Siempre se va mostrar")
}

//Lanza un error
throw {
    error: "Esta",
    info: "Tambien"
}