// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

error MayorQueCero();

contract ErroresPersonalizados {
    int private numero;

    mapping(int => string) cambio;

    function mayorACero(int _numero) external returns (string memory) {
        numero = _numero;
        if (numero > 0) {
            string memory felicitar = "Muy bien";
            return felicitar;
        } else {
            revert MayorQueCero();
        }
    }
}
