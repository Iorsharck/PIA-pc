import hashlib
import base64
from cryptography.fernet import Fernet
from PIL import Image
import argparse
import logging
import metadatos_imag

logging.basicConfig(filename='imagenFernet.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

descripcion="Retorna un mensaje des/encriptado de key de Fernet con base en una imagen"
epilogo="""Advertencia: Este programa usa como formato de imagen valido JPG
        + Retornar mensaje encriptado con imagen
            --mensaje "Hola mundo" --modo "encriptar"
		+ Retornar mensaje desencriptado con imagen
		    -- path "C:/Users/Admin/Pictures/x.png" --mensaje "=xQlhn=" --modo "desencriptar" """
parser = argparse.ArgumentParser(description=descripcion, epilog=epilogo,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-me","--mensaje", help="Mensaje para des/encriptar", required=True, type=str)
parser.add_argument("-m","--modo",help="Modo de ejecucion: encriptar, desencriptar", required=True, type=str, choices=['encriptar','desencriptar'])
params = parser.parse_args()

def generateKey(pathImage):
    try:
        img = Image.open(pathImage)
        # Convertimos la imagen a escala de grises para simplificar
        img_gray = img.convert('L')
        # Obtenemos los datos de los píxeles de la imagen en forma de bytes
        pixels = img_gray.tobytes()
        # Generamos un hash SHA-256
        hash_bytes = hashlib.sha256(pixels).digest()
        # Nos aseguramos de que la clave tenga una longitud de 32 bytes
        key = base64.urlsafe_b64encode(hash_bytes)
    except Exception as e:
        logging.error("Algo salio mal con la generacion de la llave. ",e)
    return key

def encryptMessage(message, key):
    try:
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message.decode()         #pone string en vez de bits
    except Exception as e:
        logging.error("Algo salio mal con la encriptacion. ",e)

def decryptMessage(encrypted_message, key):
    try:
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        return decrypted_message
    except Exception as e:
        logging.error("Algo salio mal con la desencriptacion. ",e)

pathImage = 'C:/Users/mennd/OneDrive/Escritorio/PIA_PCPC/NUEVOS/imagen_bonita.jpg'

if (params.modo == "encriptar"):
    print(encryptMessage(params.mensaje,generateKey(pathImage)))
    msg1 = "este es el mensaje cifrado"
    msg2 = encryptMessage(params.mensaje,generateKey(pathImage))
    metadatos_imag.meter_metadatos(msg1, msg2)
    image_modi = "imagen_bonita.jpg"
    metadatos_imag.imprimir_metasmodi(image_modi)


if (params.modo == "desencriptar"): print('\n',decryptMessage(params.mensaje,generateKey(pathImage)).decode())


