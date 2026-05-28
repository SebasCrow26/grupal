# Guion de Presentacion - Grupal DeFi

**Julian Duarte - Sebastian Ramos - Alejandra Rivera**  
**DeFi 1 - Universidad Externado de Colombia**

---

## Apertura - El Problema (1-2 min)

> Hablar con calma, mirando al publico. No leer palabra por palabra.

"Seguramente les ha pasado: estan planeando un viaje con amigos, alguien se ofrece a recibir el dinero, y empieza el caos. Transferencias que no llegan, el que dice que ya pago pero nadie sabe, el momento incomodo de cobrarle al amigo por tercera vez.

Ese problema tan cotidiano, esa vaca, es exactamente lo que quisimos resolver. Pero no con una hoja de Excel ni con un grupo de WhatsApp, sino con una logica transparente apoyada en blockchain y contratos inteligentes.

Nuestro proyecto se llama **Grupal**. Es un prototipo academico de una plataforma fintech descentralizada para manejar fondos colectivos: desde que se crea el fondo, hasta que se completan los aportes y se liberan los recursos."

---

## Que Es Grupal - Vision General (1 min)

"Grupal tiene tres componentes que trabajan juntos:

El primero es la **interfaz de usuario**, una app movil simulada donde cualquier persona puede crear un fondo, ver participantes, revisar aportes, consultar historial y simular una tarjeta virtual grupal.

El segundo es el **motor en Python**, que representa la capa que en un producto real conectaria la app con la blockchain usando Web3.py. En nuestra demo, ese motor simula el ciclo completo: crear fondo, registrar aportes, verificar la meta, liberar recursos y mostrar un resumen auditable.

El tercero es el **Smart Contract en Solidity**, llamado `VacaPool`. Este contrato guarda las reglas principales del fondo: quien lo creo, cual es la meta, cuanto se ha recaudado, cuanto aporto cada direccion y bajo que condicion se puede liberar el dinero."

---

## El Smart Contract - Como Funciona (3-4 min)

> Parte tecnica. Conviene mostrar `contracts/VacaPool.sol`.

"Expliquemos el Smart Contract con la historia de un grupo que va a Cartagena.

Un Smart Contract es como un acuerdo automatico que vive en blockchain. No depende de que una persona diga 'confien en mi', sino de reglas visibles en codigo.

Nuestro contrato se llama `VacaPool` y tiene una estructura principal llamada `Fund`. Esa estructura guarda:

- el titulo del fondo,
- la meta,
- el monto recaudado,
- el creador,
- si el fondo ya esta completo,
- y si los recursos ya fueron liberados.

Ademas, usamos dos `mappings`. Uno guarda los fondos por ID, y otro registra cuanto aporto cada direccion a cada fondo. Eso permite auditar los aportes.

El contrato emite cuatro eventos importantes:

- `FundCreated`, cuando se crea un fondo.
- `ContributionReceived`, cuando alguien aporta.
- `FundCompleted`, cuando se alcanza la meta.
- `FundsReleased`, cuando se libera el dinero al destinatario.

El flujo es este:

Primero, el creador llama `createFund()`. El contrato valida que la meta sea mayor a cero, crea el fondo y emite el evento `FundCreated`.

Segundo, los participantes aportan con `contribute()`. El contrato recibe el valor, registra el aporte por direccion y actualiza el acumulado.

Tercero, cuando el acumulado llega a la meta, el contrato marca el fondo como completo y emite `FundCompleted`.

Cuarto, cuando el fondo ya esta completo, el creador puede llamar `releaseFunds()`. Esa funcion libera el dinero al destinatario y marca el fondo como liberado para evitar que se pague dos veces.

Y si queremos consultar el estado, tenemos `getProgress()` para ver recaudado contra meta y `getFundStatus()` para ver el estado completo que necesita la app."

---

## El Motor Python - Puente Simulado con Blockchain (2-3 min)

> Mostrar `backend/motor.py` y correr `python backend/motor.py`.

"El contrato vive en blockchain, pero una aplicacion necesita una capa que traduzca las acciones del usuario a operaciones tecnicas. Esa capa es nuestro motor en Python.

En una version real, aqui usariamos Web3.py para conectarnos a Polygon, cargar el ABI del contrato, firmar transacciones y escuchar eventos. En esta demo no usamos llaves privadas ni dinero real; simulamos el proceso para explicar el flujo.

El motor hace seis pasos:

1. Simula la conexion con Polygon y el contrato `VacaPool`.
2. Crea un fondo llamado `Viaje Cartagena`.
3. Registra tres aportes de $600.000 COP.
4. Verifica que la meta de $1.800.000 COP se completo.
5. Simula la liberacion del dinero hacia un destinatario.
6. Imprime un resumen auditable con aportes y porcentajes.

Cada operacion genera un hash simulado. En blockchain real, ese hash seria el recibo unico de la transaccion. Aqui lo usamos para mostrar trazabilidad."

Comando para la demo:

```bash
python backend/motor.py
```

---

## La App - Demo en Vivo (1-2 min)

> Abrir `app/presentacion.html` en el navegador.

"Ahora lo vemos desde la perspectiva del usuario.

Esta vista carga la app dentro de un mockup de telefono. En el dashboard podemos ver fondos activos, progreso, participantes y actividad.

El fondo `Viaje Cartagena` muestra como se ve una vaca en proceso. Se puede abrir el detalle, revisar quien pago, ver el hash simulado y entender cual es la siguiente accion del fondo.

La tarjeta virtual grupal representa el resultado de completar las reglas del fondo. La idea es que el dinero no se use porque alguien lo pidio por chat, sino porque el sistema verifico que se cumplio la condicion.

Tambien hay una seccion de inversion conjunta, donde el proyecto muestra como se podrian repartir rendimientos proporcionalmente al aporte de cada participante."

---

## Marco Legal - Por Que Importa (1 min)

"Una parte importante del proyecto es reconocer el limite legal.

En Colombia, captar dinero del publico sin autorizacion de la Superintendencia Financiera puede ser ilegal. Por eso Grupal se plantea como una capa tecnologica y no como una entidad que custodia dinero real.

En un producto real, el dinero tendria que moverse a traves de una entidad regulada, como un banco, una billetera autorizada o una alianza financiera. La blockchain funcionaria como registro de reglas, trazabilidad y auditoria.

Tambien modelamos ideas de KYC y cumplimiento para mostrar que un proyecto fintech no solo es codigo: tambien necesita regulacion, seguridad y responsabilidad."

---

## Cierre (30 seg)

"En resumen, Grupal toma un problema cotidiano, la vaca, y lo convierte en un flujo mas transparente:

crear fondo, recibir aportes, verificar la meta, liberar recursos y dejar trazabilidad.

La propuesta combina una interfaz facil de usar, un motor Python que simula la conexion con blockchain y un contrato inteligente que define las reglas del fondo.

El repositorio queda organizado para revisar la app, el contrato, el motor y los documentos academicos."

---

## Posibles Preguntas y Respuestas

**Por que Polygon y no Ethereum directamente?**  
"Ethereum puede tener costos de gas altos para pagos pequenos. Polygon mantiene compatibilidad con herramientas del ecosistema Ethereum y permite transacciones mas baratas, lo cual tiene mas sentido para aportes grupales de bajo monto."

**El contrato maneja pesos colombianos reales?**  
"No. El contrato esta escrito para recibir valor en una red compatible con Ethereum. En la demo usamos pesos colombianos para explicar montos al usuario, pero la integracion real requeriria una pasarela, una entidad regulada o una moneda/token compatible."

**Que pasa si alguien no paga?**  
"El contrato no puede obligar a una persona a pagar. Lo que si puede hacer es mantener el fondo sin liberar hasta que se cumpla la regla definida. La app muestra pendientes y permite simular recordatorios o decisiones del grupo."

**Quien puede liberar el dinero?**  
"En esta demo, la funcion `releaseFunds()` permite que el creador libere el fondo cuando la meta ya se cumplio. Lo mantuvimos asi para que el contrato sea claro en clase. En una version mas avanzada podria usarse votacion, multisig o reglas de consenso mas completas."

**Es seguro guardar dinero en un contrato?**  
"Un contrato puede ser auditable, pero para usar dinero real necesitariamos pruebas, auditoria, control de permisos y cumplimiento regulatorio. Por eso el proyecto se presenta como prototipo academico."

**En que se diferencia de dividir cuentas en una app tradicional?**  
"Dividir cuentas solo calcula cuanto debe pagar cada persona. Grupal modela un fondo con reglas: registra aportes, verifica la meta, mantiene trazabilidad y muestra como podria liberarse el dinero bajo condiciones definidas."

---

**Tiempo total estimado:** 10-12 minutos + preguntas.
