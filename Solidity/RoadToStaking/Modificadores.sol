// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract modificadores {
    string private nombre;
    string private apellido;
    address private admin;

    constructor() {
        admin = msg.sender;
    }

    function setNombre(
        string memory _nombre,
        uint256 edad
    ) external mayorACero(edad) {
        nombre = _nombre;
    }

    function setApellido(
        string memory _apellido,
        uint256 edad
    ) external mayorACero(edad) {
        apellido = _apellido;
    }

    function getNombre() external view soloAdmin returns (string memory) {
        return nombre;
    }

    modifier mayorACero(uint256 edad) {
        require(edad > 0);
        _;
    }

    modifier soloAdmin() {
        require(admin == msg.sender);
        _;
    }
}
