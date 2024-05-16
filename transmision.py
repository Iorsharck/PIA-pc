import socket
import argparse
import logging

logging.basicConfig(filename='transmision.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

descripcion="Recibe bytes para enviar o guardaar una imagen de una IP y puerto en TCP"
epilogo="""Ejemplo de uso:
		+ Enviar la imagen cat0.jpg
            --modo "cliente" --path "C:\Users\Admin\Downloads\cat0.jpg"
		+ Recibir imagen y guardarla como gato.jpg
			--modo "servidor" --path "C:\Users\Admin\Downloads\gato.jpg"
		+ Recibir imagen con puerto, ip y buffer size:
			--modo "servidor" --path "C:\Users\Admin\Downloads\gato.jpg" --ip "127.0.0.1" --puerto "5005" --bufferS 4000 """ 
parser = argparse.ArgumentParser(description=descripcion, epilog=epilogo,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-i","--ip", metavar='IP',
                     help="IP del: remitente (sender)[modo \"servidor\"] , destinatario (receiver)[modo \"cliente\"]",
                     default="127.0.0.1", type=str)
parser.add_argument("-po","--puerto", help="Puerto a transmitir", default="5005", type=int)
parser.add_argument("-bz","--bufferS", metavar='SIZE', help="Tamaño del buffer", default="6000000", type=int)
parser.add_argument("-pa","--path",metavar= "JPG", help="Archivo destino", required=True, type=str)
parser.add_argument("-m","--modo",help="Modo de ejecucion: servidor,cliente", required=True, type=str, choices=['cliente','servidor'])
params = parser.parse_args()

def receiver(ip,puerto,bz,rutabai): #Receiver, Servidor

    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((ip,puerto))
        servidor.listen(1)

        (cliente, clienteaddr) = servidor.accept()
        logging.info(f"Servidor-- Estamos conectando con: {ip}")
        try:
            bytes = cliente.recv(bz)
        except Exception as e:
            logging.error("Algo salio mal al recibir los bytes. ",e)
    except Exception as e:
        logging.error("Algo salio mal con la conexion. ",e)

    try:
        with open(rutabai, 'wb') as f:
            f.write(bytes)
    except Exception as e:
        logging.error("Algo salio mal al guardar el archivo ",e)

    logging.info(f"Servidor--- La imagen se guardo en {str(rutabai)}")
    cliente.close()
    servidor.close()
    logging.info(f'Servidor---- Ah finalizado la conexión')#Editar

def sender(ip,puerto,rutaiab): #Sender, cliente

    logging.debug(f"Cliente-- Iniciando")#Editar esto

    try:
        cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip,puerto))

        try:
            with open(rutaiab, 'rb') as f:
                imagenb = f.read()
        except Exception as e:
            logging.error("Algo salio mal con el archivo. ",e)

        timagen = len(imagenb)
        try:
            cliente.sendall(imagenb)
        except Exception as e:
            logging.error("Algo sucedio mal con el envio de la imagen. ",e)


        logging.info(f'Cliente-- El tamaño de la imagen es de {timagen} bytes')
        cliente.close()
        logging.info(f"Cliente--- Finalizado cliente")#Editar esto
    except Exception as e:
        logging.error("Algo sucedio mal con la conexion. ",e)

if params.modo=="servidor":receiver(params.ip,params.puerto,params.bufferS,params.path)
if params.modo=="cliente":sender(params.ip,params.puerto,params.path)