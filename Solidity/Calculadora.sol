// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract Calculadora {
    function suma(
        uint256 valor1,
        uint256 valor2
    ) public pure returns (uint256) {
        return valor1 + valor2;
    }

    function resta(
        uint256 valor1,
        uint256 valor2
    ) public pure returns (uint256) {
        return valor1 - valor2;
    }

    function multiplicacion(
        uint256 valor1,
        uint256 valor2
    ) public pure returns (uint256) {
        return valor1 * valor2;
    }

    function division(
        uint256 valor1,
        uint256 valor2
    ) public pure returns (uint256) {
        return valor1 / valor2;
    }
}
