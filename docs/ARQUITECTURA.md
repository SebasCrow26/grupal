# Arquitectura del proyecto

Grupal se organiza en tres capas que separan la experiencia de usuario, la simulacion backend y la logica blockchain.

## 1. Frontend - `app/`

El archivo `app/index.html` contiene la aplicacion movil simulada. Esta construido como un prototipo autocontenido para que el profesor pueda abrirlo sin instalar dependencias.

Responsabilidades principales:

- Mostrar fondos activos, pendientes y completos.
- Simular aportes de participantes.
- Calcular progreso de cada fondo.
- Mostrar historial con hashes simulados.
- Simular autorizaciones para activar una tarjeta grupal.
- Mostrar el cierre del fondo cuando la meta se cumple.
- Presentar un modulo de inversion con ganancias proporcionales.
- Explicar restricciones legales dentro de la app.

El archivo `app/presentacion.html` no contiene logica de negocio. Solo envuelve la app en un mockup de telefono para que la presentacion se vea profesional.

## 2. Backend simulado - `backend/`

El archivo `backend/motor.py` representa la capa que en un producto real conectaria la app con blockchain.

Responsabilidades principales:

- Simular conexion con un nodo de Polygon.
- Simular creacion de fondos.
- Recibir un aporte desde la app.
- Generar un hash de transaccion simulado.
- Verificar si el fondo alcanzo la meta.
- Activar el siguiente paso cuando el fondo llega al 100%.
- Simular la liberacion final de recursos.

En produccion, esta capa usaria Web3.py, variables de entorno para llaves/RPC, manejo de errores, confirmaciones de red y persistencia en base de datos.

## 3. Smart contract - `contracts/`

El archivo `contracts/VacaPool.sol` es el nucleo verificable del proyecto.

Funciones principales:

- `createFund`: crea un fondo con titulo, meta y creador.
- `contribute`: recibe ETH, registra aportes por direccion y actualiza el acumulado.
- `releaseFunds`: libera el dinero cuando la meta se completa y evita dobles retiros.
- `getProgress`: devuelve el valor recaudado y la meta del fondo.
- `getFundStatus`: devuelve el estado que necesita la app para explicar el ciclo completo.

Eventos:

- `FundCreated`: deja registro de la creacion del fondo.
- `ContributionReceived`: registra cada aporte.
- `FundCompleted`: marca que la meta se cumplio.
- `FundsReleased`: registra que el dinero fue entregado al destinatario.

## Flujo general

```text
Usuario en la app
    ↓
Frontend valida datos y muestra experiencia simple
    ↓
Motor Python simula firma/envio de transaccion
    ↓
Contrato Solidity registra aporte y estado del fondo
    ↓
Cuando la meta se cumple, el contrato permite releaseFunds
    ↓
App muestra progreso, hash y cierre del fondo
```

## Limitaciones tecnicas aceptadas

Por ser un trabajo universitario, el proyecto prioriza claridad conceptual y demostracion sobre integracion productiva. Las limitaciones principales son:

- No hay despliegue permanente del contrato.
- No hay wallet real conectada al frontend.
- No hay backend HTTP ni base de datos.
- No hay pruebas automatizadas.
- Los hashes del frontend y Python son simulados.

Estas limitaciones deben mencionarse en la presentacion como decisiones de alcance, no como fallas del concepto.
