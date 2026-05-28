// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title VacaPool
 * @dev Contrato Inteligente para la gestión descentralizada de fondos grupales (La Vaca).
 * Diseñado para la clase DeFi 1 - Universidad Externado de Colombia.
 */
contract VacaPool {
    
    struct Fund {
        string title;
        uint256 goalAmount;
        uint256 currentAmount;
        address creator;
        bool isComplete;
    }
    
    mapping(uint256 => Fund) public funds;
    mapping(uint256 => mapping(address => uint256)) public contributions;
    
    uint256 public fundCount = 0;
    
    event FundCreated(uint256 id, string title, uint256 goalAmount, address creator);
    event ContributionReceived(uint256 fundId, address contributor, uint256 amount);
    event FundCompleted(uint256 fundId);
    
    /**
     * @dev Crea un nuevo fondo (vaca) con una meta específica.
     */
    function createFund(string memory _title, uint256 _goalAmount) public {
        require(_goalAmount > 0, "La meta debe ser mayor a 0");
        
        fundCount++;
        funds[fundCount] = Fund({
            title: _title,
            goalAmount: _goalAmount,
            currentAmount: 0,
            creator: msg.sender,
            isComplete: false
        });
        
        emit FundCreated(fundCount, _title, _goalAmount, msg.sender);
    }
    
    /**
     * @dev Permite a los usuarios aportar a un fondo específico.
     */
    function contribute(uint256 _fundId) public payable {
        Fund storage f = funds[_fundId];
        require(!f.isComplete, "El fondo ya alcanzo su meta");
        require(msg.value > 0, "Debes enviar un monto valido");
        
        f.currentAmount += msg.value;
        contributions[_fundId][msg.sender] += msg.value;
        
        emit ContributionReceived(_fundId, msg.sender, msg.value);
        
        // Regla del Smart Contract (Consenso Automático)
        if(f.currentAmount >= f.goalAmount) {
            f.isComplete = true;
            emit FundCompleted(_fundId);
            // Aqui se liberaria la tarjeta virtual o se ejecutaria el pago DeFi.
        }
    }
    
    /**
     * @dev Consulta el progreso actual de un fondo.
     */
    function getProgress(uint256 _fundId) public view returns (uint256, uint256) {
        return (funds[_fundId].currentAmount, funds[_fundId].goalAmount);
    }
}
