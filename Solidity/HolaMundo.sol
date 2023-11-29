// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract HolaMundo {
    string private usuario;

    function agregarUsuario(string memory _usuario) public {
        usuario = _usuario;
    }

    function saludarUsuario() public view returns (string memory) {
        string memory saludo1 = " este es tu 'Hola ";
        string memory saludo2 = "Mundo'";
        string memory saludo = string(
            abi.encodePacked(usuario, saludo1, saludo2)
        );

        return saludo;
    }
}
