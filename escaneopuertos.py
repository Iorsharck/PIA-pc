import socket
import logging
import argparse

logging.basicConfig(filename='port_scanner.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

parser = argparse.ArgumentParser(description = "Escaneo de puertos", 
formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--host", help = "Dirección IP para escanear", default="127.0.0.1")
args = parser.parse_args()

p_abiertos = 0
# Diccionario de Puertos
puertos = dict()
puertos = {
    20: "FTP Data", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 59: "DCC", 79: "Finger", 
    80: "HTTP", 110: "POP3", 113: "IDENT", 119: "NNTP", 135: "NetBIOS", 139: "NetBIOS", 143: "IMAP", 389: "LDAP",
    443: "HTTPS", 445: "MSFT DS", 563: "POP3 SSL", 993: "IMAP4 SSL", 995: "POP3 SSL", 1080: "Proxy", 1723: "PPTP",
    3306: "MySQL", 5000: "UPnP", 445: "prueba", 8080: "Proxy Web"}

print("#" + (" " * 9) + "Escaner de Puertos con Python" + (" " * 9) + "#")


def scan_ports(host):
    puertos_abiertos = {}
    for puerto,nombre in puertos.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            resultado = s.connect_ex((host, puerto))
            if resultado == 0:
                puertos_abiertos[puerto] = nombre
            s.close()
        except socket.error as e:
            logging.error(f"Error al escanear el puerto {puerto, nombre}: {e}")
            print(f"Error al escanear el puerto {puerto, nombre}: {e}")
    return puertos_abiertos

if __name__ == "__main__":
    
    try:
        puertos_abiertos = scan_ports(args.host)
        if puertos_abiertos:
            print("Puertos abiertos en", args.host + ":")
            for puert,nombr in puertos_abiertos.items():
                print("- tienes este puerto abierto %s - %s  " %(puert,nombr) )
        else:
            print("No se encontraron puertos abiertos en", args.host)
    except Exception as e:
        logging.error(f"Error durante el escaneo de puertos: {e}")
