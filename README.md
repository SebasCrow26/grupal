# Grupal — Finanzas Grupales con Blockchain

Proyecto final de DeFi 1 — Universidad Externado de Colombia  
Julián Duarte y Sebastián Ramos · Mayo 2026

---

## La idea

Todo empezó con un problema que todos hemos vivido: alguien del grupo recoge la plata para un viaje o una cena, y siempre termina en drama. Quién pagó, cuánto falta, a quién le falta pagar.

La pregunta que nos hicimos fue: ¿y si en vez de depender de una persona, el dinero lo administra un contrato en blockchain que no puede mentir ni favorecer a nadie?

Eso es Grupal. Una simulación de cómo se vería una app fintech colombiana donde los fondos grupales los gestiona un Smart Contract en Solidity, con un motor en Python que conecta los pagos con la blockchain, y una interfaz móvil donde el usuario no necesita saber nada de crypto para usarla.

---

## Archivos del proyecto

```
VacaPool.sol          → el contrato inteligente (el corazón del proyecto)
index.html            → la app simulada, se abre directo en el navegador
presentacion.html     → versión demo con mockup de teléfono, para presentar
motor.py              → simula la conexión con el nodo y el procesamiento de pagos
reporte.tex           → reporte técnico completo
grupal_maestro.docx   → documento maestro con flujos, legal y arquitectura
```

---

## El Smart Contract (VacaPool.sol)

Está escrito en Solidity 0.8 y desplegable en cualquier red compatible con Ethereum. Lo probamos en Remix IDE sobre la red de prueba Sepolia.

Tiene tres funciones:

**createFund** — crea el fondo con un nombre y una meta en Wei. Cualquiera puede crear un fondo, el contrato le asigna un ID automático.

**contribute** — recibe ETH directamente. El contrato registra cuánto aportó cada dirección y actualiza el acumulado. Si el fondo ya llegó a la meta, rechaza aportes nuevos.

**getProgress** — devuelve el estado actual del fondo: cuánto hay y cuánto falta.

Cuando el acumulado llega a la meta, el contrato emite el evento `FundCompleted`. En un escenario real, ahí se dispararía la activación de la tarjeta débito grupal o el pago al destinatario.

Para probarlo en Remix:
1. Abrir [remix.ethereum.org](https://remix.ethereum.org) y cargar `VacaPool.sol`
2. Compilar con la versión `0.8.x`
3. Desplegar en Remix VM o Sepolia testnet
4. Llamar `createFund("nombre", 1000000000000000000)` — el número es 1 ETH en Wei
5. Desde otra cuenta, llamar `contribute(1)` enviando ETH como value
6. Ver el progreso con `getProgress(1)`

---

## El motor Python (motor.py)

Python actúa como la capa intermedia entre lo que el usuario hace en la app y lo que ocurre en el contrato. En producción real usaríamos Web3.py para conectarnos al nodo; acá lo simulamos para mostrar el flujo.

Tiene tres funciones:

**simular_conexion_blockchain** — modela la latencia de conectarse al nodo de Polygon. En real, aquí va la instancia de Web3 con el RPC del nodo.

**procesar_aporte** — recibe el nombre del usuario, el monto y el ID del fondo. Simula la firma criptográfica de la transacción y genera un hash con SHA-256 para que el demo sea realista. En producción, este hash lo devuelve la red al confirmar la transacción.

**verificar_estado_fondo** — implementa la misma regla del contrato pero del lado Python: si el recaudado llega al 100% de la meta, activa la tarjeta. Si no, avisa cuánto falta.

Para correrlo:
```bash
python motor.py
```

El script trae un ejemplo cargado: un aporte de Sebastián Ramos por $600,000 COP a un fondo que ya llegó a su meta.

---

## La app (index.html)

Se abre directo en el navegador, sin instalar nada. Simula una billetera fintech móvil con fondos activos, historial de transacciones con hashes simulados, calculadora de rentabilidad, tarjeta virtual grupal y un módulo de inversión conjunta con rendimientos proporcionales.

Para la demo de presentación usar `presentacion.html` — carga la app dentro de un mockup de iPhone.

---

## Por qué Polygon y no Ethereum directamente

Los costos de gas en Ethereum mainnet hacen inviable cobrar cuotas pequeñas — una transacción puede costar más que el aporte mismo. Polygon es una red capa 2 sobre Ethereum que reduce esos costos a fracciones de centavo manteniendo la misma seguridad. Para un producto como este, donde la gente aporta desde $50,000 COP, eso es determinante.

---

## Limitación legal importante

Este es un simulador académico. Para operar en Colombia con dinero real, la plataforma no puede recibir fondos directamente sin autorización de la Superintendencia Financiera (Decreto 663 de 1993). El modelo viable es aliarse con una entidad regulada como Nequi o Bancolombia que custodie el dinero, mientras Grupal actúa como la capa tecnológica encima. El Smart Contract registra todo, pero el dinero físico siempre fluye por canales regulados.

---

*"La blockchain no miente, no se cansa y no se queda con la plata."*
