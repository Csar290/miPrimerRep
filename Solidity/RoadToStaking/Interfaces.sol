// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

//Importaciones/Librerias
//import "./Modificadores.sol";

interface ICarretera {
    function getRutaA() external view returns (string memory);
}

//1
/*is modificadores*/ contract Coche {
    string private nombre;
    ICarretera iCarretera; //Declaracion de la interfaz

    constructor(address _carretera) {
        iCarretera = ICarretera(_carretera);
    }

    function setName(string memory _nombre) external returns (string memory) {
        nombre = _nombre;
        return nombre;
    }

    function getName() external view returns (string memory) {
        return nombre;
    }

    function getRutaA() external view returns (string memory) {
        return iCarretera.getRutaA();
    }
}

//2
contract Carretera {
    string private rutaA;
    string private rutaB;

    constructor() {
        rutaA = "Lima-Callao";
        rutaB = "Lima-Chiclayo";
    }

    function getRutaA() external view returns (string memory) {
        return rutaA;
    }

    function getRutaB() external view returns (string memory) {
        return rutaB;
    }
}
