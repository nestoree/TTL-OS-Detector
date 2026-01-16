import os
import platform
import re

def obtener_ttl(destino):

    if platform.system().lower() == "windows":
        comando = f"ping -n 1 {destino}"
    else:
        comando = f"ping -c 1 {destino}"
    
    proceso = os.popen(comando)
    salida = proceso.read()
    proceso.close()

    ttl = re.search(r"ttl=(\d+)", salida, re.IGNORECASE)
    if ttl:
        return int(ttl.group(1))
    else:
        return None

def detectar_sistema_operativo(ttl):
    if ttl is None:
        return "No se pudo obtener el TTL."
    elif ttl == 128:
        return "Probablemente Windows."
    elif ttl == 64:
        return "Probablemente Linux o macOS."
    elif ttl == 255:
        return "Probablemente un dispositivo de red (Cisco u otros)."
    else:
        return "Sistema operativo desconocido o TTL personalizado."

destino = input("Escribe la IP de la que quieras su ttl: ")
ttl = obtener_ttl(destino)
sistema_operativo = detectar_sistema_operativo(ttl)

print(f"TTL detectado: {ttl}")
print(f"Sistema operativo estimado: {sistema_operativo}")
