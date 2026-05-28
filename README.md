# Grupal - Finanzas Grupales con Blockchain

Proyecto final de DeFi 1 - Universidad Externado de Colombia  
Julian Duarte y Sebastian Ramos - Mayo 2026

Grupal es un prototipo academico de una app fintech para administrar "vacas" o fondos grupales con reglas transparentes. La idea central es sencilla: el grupo define una meta, cada participante aporta, y un contrato inteligente registra el avance para que nadie dependa de pantallazos, memoria o confianza ciega.

## Ruta recomendada para el profesor

1. Abrir la demo visual: [app/presentacion.html](app/presentacion.html)
2. Revisar la app completa: [app/index.html](app/index.html)
3. Leer el contrato inteligente: [contracts/VacaPool.sol](contracts/VacaPool.sol)
4. Ejecutar la simulacion Python: [backend/motor.py](backend/motor.py)
5. Consultar los documentos academicos: [docs/](docs/)

## Estructura del repositorio

```text
.
├── app/
│   ├── index.html          # Aplicacion movil simulada
│   └── presentacion.html   # Demo en mockup de telefono para sustentacion
├── backend/
│   └── motor.py            # Simulacion del ciclo crear-aportar-liberar
├── contracts/
│   └── VacaPool.sol        # Smart contract principal del proyecto
├── docs/
│   ├── ARQUITECTURA.md     # Explicacion tecnica y flujo del sistema
│   ├── Reporte.pdf         # Reporte final procesado
│   └── grupal_maestro.docx # Documento maestro
├── LICENSE
└── README.md
```

## Que entrega el proyecto

- **Smart contract en Solidity:** crea fondos, recibe aportes, marca metas completas y libera recursos al destinatario.
- **Motor Python:** simula la capa backend que conectaria una app real con Web3.py y un nodo de Polygon.
- **Aplicacion HTML/CSS/JS:** prototipo navegable de una billetera grupal con fondos, aportes, historial, tarjeta virtual, autorizaciones, inversiones y modulo legal.
- **Documentacion academica:** reporte final en PDF, documento maestro y arquitectura.

## Como probar cada parte

### Demo visual

Abrir en el navegador:

```text
app/presentacion.html
```

Esa vista carga `app/index.html` dentro de un mockup de telefono para que la sustentacion se vea ordenada.

### App completa

Abrir directamente:

```text
app/index.html
```

No necesita servidor ni instalacion. Todo corre en el navegador y usa `localStorage` para guardar fondos creados durante la demo.

### Motor Python

Desde la raiz del repo:

```bash
python backend/motor.py
```

El script imprime el flujo completo: conexion, creacion del fondo, aportes, hashes simulados, validacion de meta, liberacion de recursos y resumen auditable.

### Smart contract

1. Abrir <https://remix.ethereum.org>
2. Cargar [contracts/VacaPool.sol](contracts/VacaPool.sol)
3. Compilar con Solidity `0.8.x`
4. Desplegar en Remix VM o Sepolia
5. Probar:
   - `createFund("Viaje Cartagena", 1000000000000000000)`
   - `contribute(1)` enviando ETH en `value`
   - `getProgress(1)`
   - `releaseFunds(1, direccion_destino)` cuando la meta este completa

## Limitacion importante

Este proyecto es un simulador academico. Para operar con dinero real en Colombia, Grupal tendria que trabajar con una entidad vigilada que custodie los fondos y cumpla procesos de KYC/AML. El contrato y la app muestran la logica de transparencia, pero no constituyen una plataforma financiera lista para produccion.

## Opinion rapida

Como trabajo universitario, el proyecto esta bien encaminado: tiene problema claro, demo visual convincente, contrato funcional, simulacion backend y discusion legal. Su punto mas fuerte es la experiencia de presentacion. Su principal limite es que todavia no integra Web3.py, wallet real ni pruebas automatizadas; para el alcance de clase, eso es aceptable si se presenta como prototipo.
