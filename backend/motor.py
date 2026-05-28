import hashlib
import time
from dataclasses import dataclass, field


"""
Motor de demostracion de Grupal.

Este archivo representa la capa backend que, en una version real, recibiria
solicitudes desde la app, firmaria transacciones con Web3.py y enviaria esas
transacciones al contrato VacaPool desplegado en Polygon o una red compatible
con Ethereum.

No usa internet, llaves privadas ni dinero real. Su objetivo para la clase es
mostrar el ciclo DeFi completo de forma entendible:

1. Crear una boveda grupal.
2. Registrar aportes.
3. Verificar si la meta se cumplio.
4. Liberar el fondo cuando la regla del contrato lo permite.
"""


@dataclass
class FondoDemo:
    """
    Modelo local que imita el estado basico guardado por VacaPool.sol.

    En Solidity, estos datos viven en el struct `Fund` y en el mapping
    `contributions`. Aqui los guardamos en Python para narrar el proceso sin
    depender de una red blockchain durante la sustentacion.
    """

    fondo_id: int
    nombre: str
    meta: int
    creador: str
    recaudado: int = 0
    completo: bool = False
    liberado: bool = False
    aportes: dict = field(default_factory=dict)


def generar_hash(evento, *valores):
    """
    Genera un hash simulado de transaccion.

    En una red real, el hash lo devuelve Polygon/Sepolia cuando la transaccion
    queda propagada. Para la demo usamos SHA-256 con los datos del evento y la
    hora actual, de manera que cada paso tenga un recibo auditable.
    """
    base = "-".join(str(v) for v in (evento, *valores, time.time()))
    return "0x" + hashlib.sha256(base.encode()).hexdigest()[:40]


def simular_conexion_blockchain():
    """
    Simula la conexion inicial con un nodo blockchain.

    En produccion, aqui estaria:
    - URL RPC de Polygon o Sepolia.
    - Instancia Web3.
    - ABI y direccion del contrato VacaPool.
    - Cuenta autorizada para firmar transacciones.
    """
    print("Conectando con Polygon / contrato VacaPool...")
    time.sleep(0.6)
    print("Conexion exitosa. Boveda grupal lista.\n")


def crear_fondo(nombre, meta, creador):
    """
    Simula la llamada a `createFund(nombre, meta)` del contrato.

    Args:
        nombre: titulo visible de la vaca.
        meta: objetivo de recaudo en COP para la demo.
        creador: persona que abre el fondo.

    Returns:
        FondoDemo con estado inicial en cero.
    """
    fondo = FondoDemo(fondo_id=1, nombre=nombre, meta=meta, creador=creador)
    tx_hash = generar_hash("createFund", nombre, meta, creador)

    print("[1] Fondo creado")
    print(f"    Nombre: {fondo.nombre}")
    print(f"    Meta: ${fondo.meta:,.0f} COP")
    print(f"    Creador: {fondo.creador}")
    print(f"    Hash simulado: {tx_hash}\n")
    return fondo


def procesar_aporte(fondo, usuario, monto):
    """
    Simula la llamada a `contribute(fondo_id)` enviando valor.

    La funcion actualiza el acumulado, registra cuanto aporto cada usuario y
    marca el fondo como completo cuando se alcanza la meta. Es la misma regla
    central que vive en Solidity.
    """
    if fondo.liberado:
        raise ValueError("No se puede aportar: el fondo ya fue liberado.")
    if fondo.completo:
        raise ValueError("No se puede aportar: la meta ya esta completa.")
    if monto <= 0:
        raise ValueError("El aporte debe ser mayor a cero.")

    fondo.aportes[usuario] = fondo.aportes.get(usuario, 0) + monto
    fondo.recaudado += monto

    tx_hash = generar_hash("contribute", fondo.fondo_id, usuario, monto)

    print("[2] Aporte confirmado")
    print(f"    Usuario: {usuario}")
    print(f"    Monto: ${monto:,.0f} COP")
    print(f"    Recaudado: ${fondo.recaudado:,.0f} / ${fondo.meta:,.0f} COP")
    print(f"    Hash simulado: {tx_hash}")

    if fondo.recaudado >= fondo.meta:
        fondo.completo = True
        print("    Evento Solidity: FundCompleted\n")
    else:
        faltante = fondo.meta - fondo.recaudado
        print(f"    Estado: faltan ${faltante:,.0f} COP\n")

    return tx_hash


def verificar_estado_fondo(fondo):
    """
    Consulta el estado que la app mostraria despues de leer `getFundStatus`.

    La idea pedagogica es separar dos momentos:
    - Recaudar no significa gastar.
    - Solo cuando la regla se cumple, el contrato permite liberar el dinero.
    """
    porcentaje = (fondo.recaudado / fondo.meta) * 100

    print("[3] Verificacion del contrato")
    print(f"    Progreso: {porcentaje:.2f}%")
    print(f"    Completo: {'si' if fondo.completo else 'no'}")
    print(f"    Liberado: {'si' if fondo.liberado else 'no'}")

    if fondo.completo and not fondo.liberado:
        print("    Accion disponible: releaseFunds(destinatario)\n")
    elif not fondo.completo:
        print("    Accion disponible: seguir recaudando\n")
    else:
        print("    Accion disponible: consultar historial\n")


def liberar_fondos(fondo, solicitante, destinatario):
    """
    Simula la llamada a `releaseFunds(fondo_id, destinatario)`.

    Para mantener la demo simple, el contrato exige que quien libera sea el
    creador del fondo. Esto representa una regla minima de control; en una
    version mas avanzada podria cambiarse por votacion del grupo.
    """
    if solicitante != fondo.creador:
        raise PermissionError("Solo el creador del fondo puede liberar recursos.")
    if not fondo.completo:
        raise ValueError("No se puede liberar: la meta aun no se cumple.")
    if fondo.liberado:
        raise ValueError("No se puede liberar: el fondo ya fue cerrado.")

    fondo.liberado = True
    tx_hash = generar_hash("releaseFunds", fondo.fondo_id, destinatario, fondo.recaudado)

    print("[4] Fondo liberado")
    print(f"    Destinatario: {destinatario}")
    print(f"    Valor enviado: ${fondo.recaudado:,.0f} COP")
    print("    Evento Solidity: FundsReleased")
    print(f"    Hash simulado: {tx_hash}\n")
    return tx_hash


def mostrar_resumen(fondo):
    """Imprime un resumen final de aportes para cerrar la sustentacion."""
    print("[5] Resumen auditable")
    for usuario, monto in fondo.aportes.items():
        participacion = (monto / fondo.recaudado) * 100 if fondo.recaudado else 0
        print(f"    {usuario}: ${monto:,.0f} COP ({participacion:.1f}%)")
    print(f"    Total recaudado: ${fondo.recaudado:,.0f} COP")
    print(f"    Estado final: {'liberado' if fondo.liberado else 'pendiente'}")


if __name__ == "__main__":
    # --- DEMOSTRACION PARA LA SUSTENTACION ---
    simular_conexion_blockchain()

    fondo_viaje = crear_fondo(
        nombre="Viaje Cartagena",
        meta=1_800_000,
        creador="Sebastian Ramos",
    )

    procesar_aporte(fondo_viaje, "Sebastian Ramos", 600_000)
    procesar_aporte(fondo_viaje, "Julian Duarte", 600_000)
    procesar_aporte(fondo_viaje, "Alejandra Rivera", 600_000)

    verificar_estado_fondo(fondo_viaje)
    liberar_fondos(
        fondo=fondo_viaje,
        solicitante="Sebastian Ramos",
        destinatario="Hotel Cartagena Demo",
    )
    mostrar_resumen(fondo_viaje)
