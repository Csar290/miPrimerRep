let contendeor1 = document.querySelector(".container1")
let contendeor2 = document.querySelector(".container2")
let button = document.querySelector(".button")

//Hover
button.addEventListener("mouseover", (evento) => {
    alert("Acabas de pasar el mouse por encima del boton")
})

//Hover out
button.addEventListener("mouseout", (evento) => {
    alert("Acabas de sacar el mouse del boton")
})

//mousemove: ocurre cuando el puntero se mueve mientras esta sobre el elemento
//mouseleave: ocurre cuando se mueve fuera del elemento
//mausedown: ocurre cuando apreta un boton del mouse(no importa donde suelte el boton)
//mouseup: ocurre cuando suelta un boton del mouse dentro del elemento

