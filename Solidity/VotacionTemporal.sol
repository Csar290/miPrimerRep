// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract VotacionTemporal {
    uint256 private startTime;
    uint256 private duration = 60;

    //Objeto con los datos
    struct Votante {
        uint256 peso;
        bool votado;
    }

    //Convertir de address a el objeto Votante
    mapping(address => Votante) votantes;

    //Se ejecuta cuando despliegas el contrato
    constructor() {
        startTime = block.timestamp; //Tiempo actual en el que se ejecuta el contrato
    }

    //Funcion para colocar la duracion en segundos
    function setDuration(uint256 newTime) external {
        duration = newTime;
    }

    //Funcion que devuelve el tiempo
    function getDuration() external view returns (uint256) {
        return duration;
    }

    //Funcion que restablece el tiempo
    function restore() external {
        startTime = block.timestamp;
    }

    //Funcion que devuelve los segundos restantes
    function timeLeft() public view returns (uint256) {
        require(startTime <= block.timestamp, "Tiempo no valido");
        uint256 difference = block.timestamp - startTime;
        uint256 rest = difference >= duration ? 0 : duration - difference;
        return rest;
    }

    //Funcion que devuelve voto que realizó dicho address
    function getVoto() external view returns (Votante memory) {
        return votantes[msg.sender];
    }

    //Funcion que procesa el voto
    function votar(uint256 _peso) external {
        //Verifica si aun no acaba el tiempo de votado
        require(timeLeft() > 0, "El tiempo de voto se ha agotado");
        Votante storage _votante = votantes[msg.sender];
        _votante.peso = _peso;
        _votante.votado = true;
    }
}
