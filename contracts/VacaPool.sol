// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title VacaPool
 * @notice Prototipo academico para administrar fondos grupales con reglas transparentes.
 * @dev El contrato modela la "boveda" de Grupal: crea fondos, recibe aportes en ETH
 * y emite eventos que permiten auditar lo ocurrido desde una interfaz o explorador.
 *
 * Alcance del prototipo:
 * - Implementa una liberacion simple del fondo al destinatario elegido.
 * - No integra monedas estables ni pesos colombianos.
 * - No reemplaza requisitos regulatorios de una fintech real.
 */
contract VacaPool {
    /**
     * @dev Estado minimo de cada fondo.
     * title: nombre visible para el grupo.
     * goalAmount: meta en Wei.
     * currentAmount: acumulado recibido en Wei.
     * creator: direccion que creo el fondo.
     * isComplete: bandera que se activa cuando currentAmount >= goalAmount.
     * isReleased: bandera que evita liberar el mismo dinero dos veces.
     */
    struct Fund {
        string title;
        uint256 goalAmount;
        uint256 currentAmount;
        address creator;
        bool isComplete;
        bool isReleased;
    }

    // funds[id] guarda los datos publicos de cada fondo.
    mapping(uint256 => Fund) public funds;

    // contributions[id][wallet] permite auditar cuanto aporto cada direccion.
    mapping(uint256 => mapping(address => uint256)) public contributions;

    // Contador incremental. El primer fondo creado queda con id = 1.
    uint256 public fundCount = 0;

    event FundCreated(uint256 id, string title, uint256 goalAmount, address creator);
    event ContributionReceived(uint256 fundId, address contributor, uint256 amount);
    event FundCompleted(uint256 fundId);
    event FundsReleased(uint256 fundId, address recipient, uint256 amount);

    /**
     * @notice Crea un nuevo fondo grupal.
     * @param _title Nombre del fondo que vera el grupo.
     * @param _goalAmount Meta del fondo expresada en Wei.
     */
    function createFund(string memory _title, uint256 _goalAmount) public {
        require(_goalAmount > 0, "La meta debe ser mayor a 0");

        fundCount++;
        funds[fundCount] = Fund({
            title: _title,
            goalAmount: _goalAmount,
            currentAmount: 0,
            creator: msg.sender,
            isComplete: false,
            isReleased: false
        });

        emit FundCreated(fundCount, _title, _goalAmount, msg.sender);
    }

    /**
     * @notice Permite aportar ETH a un fondo existente.
     * @dev `msg.value` es el valor enviado junto con la transaccion. Si el aporte
     * hace que el fondo alcance o supere la meta, el fondo queda marcado como completo.
     * @param _fundId Identificador del fondo al que se quiere aportar.
     */
    function contribute(uint256 _fundId) public payable {
        require(_fundId > 0 && _fundId <= fundCount, "El fondo no existe");

        Fund storage f = funds[_fundId];
        require(!f.isComplete, "El fondo ya alcanzo su meta");
        require(!f.isReleased, "El fondo ya fue liberado");
        require(msg.value > 0, "Debes enviar un monto valido");

        f.currentAmount += msg.value;
        contributions[_fundId][msg.sender] += msg.value;

        emit ContributionReceived(_fundId, msg.sender, msg.value);

        // Regla central del prototipo: al cumplir la meta, el fondo se bloquea como completo.
        if (f.currentAmount >= f.goalAmount) {
            f.isComplete = true;
            emit FundCompleted(_fundId);
            // En la demo, este evento representa que la tarjeta o pago ya puede activarse.
        }
    }

    /**
     * @notice Libera el dinero de un fondo completo hacia un destinatario.
     * @dev Esta funcion cierra el ciclo financiero de la demo: la boveda recibe
     * aportes y solo cuando la meta se cumple permite entregar el dinero.
     *
     * Para mantenerlo simple en clase, solo el creador del fondo puede liberar
     * los recursos. En una version mas avanzada, esta regla podria cambiarse por
     * votacion de participantes, multisig o integracion con una tarjeta.
     *
     * @param _fundId Identificador del fondo.
     * @param _recipient Direccion que recibe el dinero acumulado.
     */
    function releaseFunds(uint256 _fundId, address payable _recipient) public {
        require(_fundId > 0 && _fundId <= fundCount, "El fondo no existe");
        require(_recipient != address(0), "Destinatario invalido");

        Fund storage f = funds[_fundId];
        require(msg.sender == f.creator, "Solo el creador puede liberar");
        require(f.isComplete, "La meta aun no se ha cumplido");
        require(!f.isReleased, "El fondo ya fue liberado");

        uint256 amount = f.currentAmount;
        f.isReleased = true;

        (bool sent, ) = _recipient.call{value: amount}("");
        require(sent, "No se pudo enviar el dinero");

        emit FundsReleased(_fundId, _recipient, amount);
    }

    /**
     * @notice Consulta el progreso de un fondo.
     * @param _fundId Identificador del fondo.
     * @return currentAmount Valor recaudado en Wei.
     * @return goalAmount Meta del fondo en Wei.
     */
    function getProgress(uint256 _fundId) public view returns (uint256 currentAmount, uint256 goalAmount) {
        require(_fundId > 0 && _fundId <= fundCount, "El fondo no existe");

        return (funds[_fundId].currentAmount, funds[_fundId].goalAmount);
    }

    /**
     * @notice Consulta el estado completo que necesita la app para pintar un fondo.
     * @dev Se agrega para que la demo pueda explicar mejor el puente Frontend -> Backend -> Solidity.
     */
    function getFundStatus(uint256 _fundId)
        public
        view
        returns (
            uint256 currentAmount,
            uint256 goalAmount,
            bool isComplete,
            bool isReleased,
            address creator
        )
    {
        require(_fundId > 0 && _fundId <= fundCount, "El fondo no existe");

        Fund storage f = funds[_fundId];
        return (f.currentAmount, f.goalAmount, f.isComplete, f.isReleased, f.creator);
    }
}
