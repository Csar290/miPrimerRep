// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract AdministrarUsuario {
    struct Usuario {
        uint256 edad;
        string nombre;
        string genero;
    }

    //Convertir de Address a el nuevo objeto Usuario
    mapping(address => Usuario) private listaDeUsuarios;

    //Funcion para registrar usuarios
    function Registrar(
        uint256 edad,
        string memory genero,
        string memory nombre
    ) public {
        Usuario storage _usuario = listaDeUsuarios[msg.sender];
        _usuario.edad = edad;
        _usuario.genero = genero;
        _usuario.nombre = nombre;
    }

    //Funcion para consultar nombre del usuario
    function Consultar() public view returns (Usuario memory) {
        return listaDeUsuarios[msg.sender];
    }

    //Funcion para eliminar usuario
    function Eliminar() public {
        delete listaDeUsuarios[msg.sender];
    }
}
