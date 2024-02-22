let contendeor1 = document.querySelector(".container1")
let contendeor2 = document.querySelector(".container2")
let button = document.querySelector(".button")

//Por defecto: Bubbling
//Se ejecuta del mas especifico(hijos) a los menos especificos(padres)
//Para alterar el orden de ejecucion
//Se coloca true como parametro

button.addEventListener("click", (evento) => {
    alert("Diste click al boton")
    evento.stopPropagation() //Detiene la propagacion de los demas eventos
})

contendeor2.addEventListener("click", (evento) => {
    alert("Diste click en el contenedor azul")
}/*, true*/)

contendeor1.addEventListener("click", (evento) => {
    alert("Diste click en el contenedor rojo")
})