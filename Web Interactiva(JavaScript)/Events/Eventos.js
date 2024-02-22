let button = document.querySelector(".button");

//evento click, dblclick o contextmenu(click derecho)
button.addEventListener("click", saludar)
function saludar() {
    alert("Holaaaaa")
}

//Tambien 
/*button.addEventListener("click", () => {
    alert("Holaaaaaaaaaaa")
})*/

/*button.addEventListener("click", (evento) => {
    console.log(evento.target)
})*/

