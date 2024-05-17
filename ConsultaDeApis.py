import requests
import logging
import argparse
import re

apikey = '4f6de85926d0c96320098fdb0b5fbe86d1f2558ced0eb962df8a527ea76bc210'
logging.basicConfig(filename='Consulta_Ips.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def validarip(ip):
    v = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if v.match(ip):
        return True
    else:
        return False


def consultaip(apikey, ip):

    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}'
    headers = {
        'x-apikey': apikey }
    response = requests.get(url, headers = headers)
    try:
        if response.status_code == 200:
            resultado = response.json()
            return resultado
        else:
            print(f'Error al consultar la IP {ip}.')
            return None
    except Exception as e:
        logging.info(f'Ocurrió un error al conectar con el servidor:{e}')


def guardarip(ip, resultado, blacklist):

    propietario = resultado['data']['attributes']['as_owner']
    categoria = resultado['data']['attributes']['last_analysis_stats']
    reporteips = 'C:/PC pero en C/PC-PIA/Reporte_Ips.txt'
    try:
        with open(reporteips, 'a') as file:
            file.write(f'IP: {ip}\n')
            file.write(f'Propietario: {propietario}\n')
            file.write(f'Malicious: {categoria['malicious']}\n')
            file.write(f'Suspicious: {categoria['suspicious']}\n')
            file.write(f'¿Esta en la blacklist? {'Sí' if blacklist else 'No'}\n\n')
        print(f'Los resultados de {ip} se han guardado en: Reporte_Ips.txt')
    except Exception as e:
        logging.info(f'Ocurrió un error al escribir los resultados...{e}')


def main():

    parser = argparse.ArgumentParser(description = 'Consulta de Ips en VirusTotal')
    parser.add_argument('ip', type = str, help = 'IP a consultar')
    args = parser.parse_args()
    ip = args.ip
    try:
        if not validarip(ip):
            print(f'La IP {ip} no es válida. Por favor, introduce una IP válida.')
            return
    except Exception as e:
        logging.info(f'Ocurrio un error al obtener la ip{e}') 
    resultado = consultaip(apikey, ip)
    try:
        if resultado:
            categoria = resultado['data']['attributes']['last_analysis_stats']
            blacklist = categoria['malicious'] > 0 or categoria['suspicious'] > 0
            if not blacklist:
                print(f'La {ip} no es maliciosa ni sospechosa.')
            else:
                print(f'La {ip} está marcada como maliciosa o sospechosa.')
            guardarip(ip, resultado, blacklist)
        else:
            print(f'No se pudo obtener resultados para la IP: {ip}')
    except Exception as e:
        logging.info(f'Ocurrió un error al imprimir los resultados.{e}')

if __name__ == "__main__":
    main()