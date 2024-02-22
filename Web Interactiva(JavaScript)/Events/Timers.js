//Ejecuta lo que esta en la funcion en el tiempo designado
/*let temporizador = setTimeout(() => {
    document.write("Acaba de pasar 3 segundos")
}, 3000)

//Cancela el temporizador
clearTimeout(temporizador)*/

//Ejecuta lo que esta en la funcion de forma infinita con intervalos del tiempo designado
let intervalo = setInterval(() => {
    document.write("Esto se ejecuta cada 5s")
}, 5000)

setTimeout(() => {
    clearInterval(intervalo)
}, 16000)
