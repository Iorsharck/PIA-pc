import socket
import logging
import argparse

logging.basicConfig(filename='port_scanner.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def scan_ports(host, port_range):
    puertos_abiertos = []
    for puerto in port_range:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            resultado = s.connect_ex((host, puerto))
            if resultado == 0:
                puertos_abiertos.append(puerto)
            s.close()
        except socket.error as e:
            logging.error(f"Error al escanear el puerto {puerto}: {e}")
            print(f"Error al escanear el puerto {puerto}: {e}")
    return puertos_abiertos

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escaneo de puertos", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("host", help="Dirección IP para escanear")
    parser.add_argument("puerto_inicial", type=int, help="Puerto de inicio del rango")
    parser.add_argument("puerto_final", type=int, help="Puerto de fin del rango")
    args = parser.parse_args()

    try:
        rango_de_puertos = range(args.puerto_inicial, args.puerto_final + 1)
        puertos_abiertos = scan_ports(args.host, rango_de_puertos)
        if puertos_abiertos:
            print("Puertos abiertos en", args.host + ":")
            for puerto in puertos_abiertos:
                print("Puerto:", puerto)
        else:
            print("No se encontraron puertos abiertos en", args.host)
    except Exception as e:
        logging.error(f"Error durante el escaneo de puertos: {e}")

