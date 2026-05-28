import time
import hashlib

def simular_conexion_blockchain():
    """Simula la latencia de conectarse al nodo de Polygon."""
    print("Conectando con el Smart Contract de Grupal (VacaPool)...")
    time.sleep(1)
    print("Conexion exitosa. Boveda lista.")
    
def procesar_aporte(usuario, monto, fondo_id):
    """
    Simula la recepcion de un aporte en Python y su envio al Smart Contract.
    Este script estaria conectado al Backend real usando Web3.py.
    """
    print(f"\n[!] Nuevo pago detectado de: {usuario}")
    print(f"[!] Monto aportado: ${monto:,.2f} COP")
    
    print(">>> Firmando transaccion criptografica...")
    time.sleep(1)
    
    # Generar un hash simulado para darle realismo a la transaccion
    tx_string = f"{usuario}-{monto}-{fondo_id}-{time.time()}"
    tx_hash = "0x" + hashlib.sha256(tx_string.encode()).hexdigest()[:40]
    
    print(f"<<< Transaccion confirmada en Blockchain. Hash: {tx_hash}")
    return tx_hash

def verificar_estado_fondo(recaudado, meta):
    """
    Verifica las reglas del consenso del grupo dictadas por el contrato inteligente.
    """
    porcentaje = (recaudado / meta) * 100
    print(f"\nEstado actual del fondo: {porcentaje}%")
    
    if porcentaje >= 100:
        print("[APROBADO] La meta se ha cumplido al 100%.")
        print(">>> Ejecutando liberacion automatica (Smart Contract)")
        print(">>> Tarjeta Virtual Grupal Activada.")
    else:
        print(f"[PENDIENTE] Faltan aportes para activar la tarjeta.")

if __name__ == "__main__":
    # --- DEMOSTRACION PARA LA SUSTENTACION ---
    simular_conexion_blockchain()
    
    # Simular un aporte
    hash_generado = procesar_aporte(usuario="Sebastian Ramos", monto=600000, fondo_id="1")
    
    # Simular la validacion del smart contract
    verificar_estado_fondo(recaudado=1800000, meta=1800000)
