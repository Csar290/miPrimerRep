let img = document.querySelector(".imagen")
let input = document.querySelector(".input")
let textoSeleccionado = document.querySelector(".seleccionado")

//Error si la imagen no carga correctamente 
img.addEventListener("error", () => {
    console.log("Ocurrio un error")
})

//Ocurre cuando un objeto ha cargado
addEventListener("load", () => {
    console.log("La pagina ha cargado")
})

//Ocurre cuando cambian el tamaño de vista del documento
addEventListener("resize", () => {
    console.log("Ha modificado el tamaño")
})

//Ocurre despues de seleccionar el texto de input o textarea
input.addEventListener("select", (evento) => {
    let start = evento.target.selectionStart
    let end = evento.target.selectionEnd
    let textoCompleto = input.value
    textoSeleccionado.textContent = textoCompleto.substring(start, end)
})

//beforeunload: ocurre antes de que te vayas de la pagina
//unload: ocurre una vez que se va de la pagina
//scroll: ocurre cuando se hace scroll
