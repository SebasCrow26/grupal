# 🐄 Grupal — Finanzas Grupales Descentralizadas

> Plataforma fintech para gestionar fondos colectivos ("vacas") mediante Smart Contracts en Ethereum.
> **Proyecto académico · DeFi 1 · Universidad Externado de Colombia**
> *Julián Duarte · Sebastián Ramos · Alejandra Rivera*

---

## ¿Qué es Grupal?

Grupal digitaliza el concepto colombiano de "hacer una vaca": un grupo de personas aporta dinero hacia una meta común. En lugar de depender de una persona que recaude el dinero, un **Smart Contract en Solidity** actúa como intermediario neutral, transparente e inmutable.

El proyecto funciona como **simulador MVP** que modela todos los flujos como si la plataforma contara con las licencias y alianzas regulatorias necesarias en Colombia.

---

## 🗂️ Estructura del Repositorio

```
grupal-defi/
│
├── VacaPool.sol          # Smart Contract principal (Solidity ^0.8.0)
├── index.html            # App móvil simulada (billetera fintech)
├── presentacion.html     # Demo con mockup de teléfono para presentación
├── motor.py              # Motor de simulación blockchain (Python)
├── reporte.tex           # Reporte técnico completo (LaTeX)
├── grupal_maestro.docx   # Documento maestro del proyecto
├── .gitignore
└── README.md
```

---

## ⚙️ Componentes del Proyecto

### 1. Smart Contract — `VacaPool.sol`

Contrato en Solidity que gestiona fondos grupales en la blockchain.

| Función | Descripción |
|---|---|
| `createFund(title, goalAmount)` | Crea un nuevo fondo con título y meta en Wei |
| `contribute(fundId)` | Aporta ETH a un fondo específico (función `payable`) |
| `getProgress(fundId)` | Consulta el monto actual vs la meta del fondo |

**Eventos emitidos:**
- `FundCreated` — cuando se crea un nuevo fondo
- `ContributionReceived` — cuando alguien realiza un aporte
- `FundCompleted` — cuando el fondo alcanza su meta (dispara activación de tarjeta)

### 2. Interfaz de Usuario — `index.html`

App web progresiva que simula una billetera fintech móvil con:
- Dashboard con saldo, fondos activos e inversiones
- Fondos grupales con barra de progreso en tiempo real
- Tarjeta débito virtual grupal con efecto flip (frente/reverso)
- Historial de transacciones con hashes de blockchain simulados
- Calculadora de rentabilidad (interés simple y compuesto)
- Sistema KYC simulado y marco legal colombiano interactivo
- Tour interactivo guiado para onboarding

### 3. Motor Python — `motor.py`

Script que simula la capa de conexión con Web3 y el Smart Contract:

```bash
python motor.py
```

Simula tres operaciones:
1. Conexión al nodo de Polygon
2. Procesamiento y firma criptográfica de un aporte
3. Verificación del consenso del fondo (reglas del contrato)

### 4. Presentación — `presentacion.html`

Demo de presentación con mockup de iPhone que renderiza la app dentro de un teléfono animado para sustentaciones.

---

## 🚀 Cómo usar

### Smart Contract (Remix IDE)

1. Abre [remix.ethereum.org](https://remix.ethereum.org/)
2. Carga `VacaPool.sol`
3. Compila con Solidity `^0.8.0`
4. Despliega en Sepolia testnet o Hardhat local

```solidity
// Crear un fondo
createFund("Viaje Cartagena", 1000000000000000000) // 1 ETH

// Contribuir (enviar ETH como value)
contribute(1)

// Consultar progreso
getProgress(1) // → (montoActual, metaTotal)
```

### App Web

Abre `index.html` directamente en el navegador. No requiere servidor.

### Motor Python

```bash
python motor.py
```

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología |
|---|---|
| Smart Contract | Solidity `^0.8.0` · Ethereum / EVM |
| Frontend | HTML · CSS · JavaScript puro |
| Motor backend | Python 3 (hashlib, time) |
| Documentación | LaTeX · Word |
| Red objetivo | Polygon (Ethereum L2) |

---

## 📐 Flujo del Sistema

```
Usuario crea fondo
       ↓
Smart Contract desplegado → hash único generado
       ↓
Participantes reciben link de invitación
       ↓
Cada quien aporta → contrato registra en blockchain
       ↓
¿currentAmount >= goalAmount?
  SÍ → FundCompleted event → flujo de autorizaciones
  NO → Recordatorios a pendientes
       ↓
Todos autorizan → Tarjeta virtual activada
       ↓
Gastos registrados en blockchain → Fondo cerrado (inmutable)
```

---

## ⚖️ Marco Legal (Colombia)

El proyecto modela el cumplimiento regulatorio necesario para operar en Colombia:

| Marco | Aplica porque... |
|---|---|
| Decreto 663/1993 (EOSF) | Grupal NO capta directamente; opera como intermediario tecnológico |
| Circular 029/2014 (SFC) | Alianza requerida con operador de pago autorizado (Nequi, Movii) |
| Ley 1581/2012 (Habeas Data) | KYC y consentimiento explícito de datos |
| SARLAFT / Resolución 885/2021 | Monitoreo y reporte UIAF para transacciones sospechosas |
| Blockchain como registro | Legal en Colombia sin autorización especial (no es moneda) |

---

## 🔮 Roadmap

| Fase | Periodo | Hitos |
|---|---|---|
| **Fase 0** — Simulador académico | Actual | App HTML funcional · Presentación en clase |
| **Fase 1** — MVP técnico | Meses 1–3 | Backend real · Smart contracts en testnet · KYC real |
| **Fase 2** — Beta | Meses 4–6 | 50–200 usuarios · Fondos reales con alianza bancaria |
| **Fase 3** — Lanzamiento | Meses 7–12 | App en producción · Tarjeta virtual real |
| **Fase 4** — Inversión | Año 2 | Módulo DeFi con instrumentos financieros regulados |
| **Fase 5** — SEDPE | Año 2–3 | Licencia SEDPE · Expansión regional |

---

## 🧹 Archivos a ignorar

Los archivos `*.Zone.Identifier` son metadatos de Windows y **no deben subirse al repo**. El `.gitignore` ya los excluye.

---

> *"La blockchain no miente, no se cansa y no se queda con la plata."* 🐄

**Universidad Externado de Colombia · DeFi 1 · Mayo 2026**
