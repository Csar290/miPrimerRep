let contendeor1 = document.querySelector(".container1")
let input = document.querySelector(".inputprueba")

input.addEventListener("keydown", (evento) => {
    console.log("Acaba de presionar una tecla")
})

input.addEventListener("keypress", (evento) => {
    console.log("Acaba de presionar y soltar una tecla")
})

input.addEventListener("keyup", (evento) => {
    console.log("Acaba soltar la tecla")
})