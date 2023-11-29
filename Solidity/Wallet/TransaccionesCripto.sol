// SPDX-License-Identifier: MIT
pragma solidity 0.8.4;

contract TransaccionesCripto {
    //Objeto con los datos
    struct Cuenta {
        uint256 saldo;
        uint256 tiempoInicio;
        uint256 tiempoBloqueo;
    }
    //Mapping Bidimensional:
    //      Direccion =>       Moneda => Cuenta
    mapping(address => mapping(bytes10 => Cuenta)) cuentas;

    //Funcion que procesa el deposito de criptos
    function depositar(
        uint256 cantidad,
        bytes10 moneda,
        uint256 tiempoBloqueo
    ) external payable {
        //La cantidad que ingresa debe ser igual a el valor que tiene
        require(msg.value == cantidad, "La cantidad no coincide");

        //Cuenta/Direccion/Moneda
        Cuenta storage _cuenta = cuentas[msg.sender][moneda];
        //Saldo + cantidad ingresada
        _cuenta.saldo += cantidad;

        _cuenta.tiempoBloqueo = tiempoBloqueo;
        _cuenta.tiempoInicio = block.timestamp;
    }

    //Funcion para retirar criptos
    function retirar(
        uint256 cantidad,
        bytes10 moneda,
        address payable wallet
    ) external {
        //Cuenta/Direccion/Moneda
        Cuenta storage _cuenta = cuentas[msg.sender][moneda];

        //Verifica que halla saldo suficiente a retirar
        require(_cuenta.saldo >= cantidad, "Saldo insuficiente");
        //Verifica si el tiempo de bloqueo se ha acabado
        require(tiempoRestante(moneda) == 0, "La moneda sigue bloqueada");

        //Llamada a la funcion para transferir cripto
        //Devuelve TRUE/FALSE
        (bool success, ) = wallet.call{value: cantidad}("");
        require(success, /*Si es false*/ "No se ha realizado el retiro");
        //Si es true
        _cuenta.saldo -= cantidad;
        _cuenta.tiempoInicio = block.timestamp;
    }

    //Funcion que devuelve los segundos restantes
    function tiempoRestante(bytes10 moneda) public view returns (uint256) {
        //Cuenta/Direccion/Moneda
        Cuenta memory _cuenta = cuentas[msg.sender][moneda];
        require(_cuenta.tiempoInicio <= block.timestamp, "Tiempo no valido");
        uint256 difference = block.timestamp - _cuenta.tiempoInicio;
        uint256 rest = difference >= _cuenta.tiempoBloqueo
            ? 0
            : _cuenta.tiempoBloqueo - difference;
        return rest;
    }

    function actualizarBloqueo(
        bytes10 moneda,
        uint256 tiempoBloqueo,
        bool reiniciar
    ) external {
        //Cuenta/Direccion/Moneda
        Cuenta storage _cuenta = cuentas[msg.sender][moneda];
        require(
            tiempoBloqueo > _cuenta.tiempoBloqueo,
            "No puedes reducir el tiempo de bloqueo"
        );
        _cuenta.tiempoBloqueo = tiempoBloqueo;

        if (reiniciar) _cuenta.tiempoInicio = block.timestamp;
    }

    //Funcion para mostrar el saldo
    function mostrarSaldo(bytes10 moneda) external view returns (uint256) {
        //Cuenta/Direccion/Moneda/Saldo
        return cuentas[msg.sender][moneda].saldo;
    }
}
