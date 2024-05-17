from pexelsapi.pexels import Pexels
import requests
from PIL import Image
import shutil
import os
import argparse
import logging
import random

logging.basicConfig(filename = 'imagenAPIPY.log',
            level = logging.INFO, format = '%(asctime)s %(message)s', 
            datefmt = '%m/%d/%Y %I:%M:%S %p')

#dafult no funciona si tienes required = True 
descripcion = "Descarga imaeges de la API de Pexels" 
epilogo = """Ejemplo de uso:
		 + Descargar una imagen random
          - [No se ocupan argumentos]
		 + Descargar 2 imagenes de robots:
			--prompt "robot" --num 2
		 + Descargar 3 imagenes de ratones usando key propia:
			--prompt "rat" --num 3 --key abcdefghjkl1023
		 + Descargar 2 imagenes de randoms:
			--prompt "random" --num 2""" 
parser = argparse.ArgumentParser(description = descripcion, epilog = epilogo,
        formatter_class = argparse.RawDescriptionHelpFormatter)
parser.add_argument("-k","--key", metavar = 'API KEY', 
                        help = "Key of the Pexels API", 
                        default = "K8yaOzBLBeEhJ830855QhUkK5HIxR61tJt3vxHnA2xOfXDmqxsnj5BbS", 
                        type = str)
parser.add_argument("-p","--prompt", help = "Prompt de la imagen", 
                        default = "random", type = str)
parser.add_argument("-n","--num", metavar = 'NUMERO DE IMAGENES', 
                        help = "Numero de imagenes", default = "1", type = int)
params = parser.parse_args()
try:
    pexel = Pexels(params.key)
except Exception as e:
        logging.error("Algo salio mal con la API .",e)


def palabrarandom(dict):
    dictionary = []
    with open(dict,"r") as dt:
        for line in dt:
            dictionary.append(str(line))
    return dictionary[random.randrange(0,len(dictionary))]


def sacar_imagenes(prompt,numero):
    download_path = str(prompt)
    try:
        search_photos = pexel.search_photos(query = prompt, orientation = '',
        size = '', color = '', locale = '', page = 1, per_page = numero)
        for i in range(len(search_photos["photos"])):
            photo = search_photos["photos"][i]
            URL_photo = photo["src"]["original"]
            response = requests.get(URL_photo,stream = True)
            try:
                response.status_code == 200
                with open(download_path + ".jpeg",'wb') as f:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, f)
                im = Image.open(download_path + ".jpeg")
                im.save((download_path) + str(i) + ".jpg")
                os.remove(download_path + ".jpeg")
                logging.info(f"Se guardo con exito el archivo {str(i)}")
            except Exception as e:
                logging.error("Algo salio mal con la conexion. ",e)
    except Exception as e:
            logging.error("Algo salio mal con la API .",e)

if __name__=="__main__":
    diccionario = "dictionary.txt"

    if params.prompt == "random":#Si quiere random
        if os.path.exists("dictionary.txt"):#Checar si esta el diccionario
            logging.info(f"Diccionnario confirmado")
            palabrita = palabrarandom(diccionario)
            palabrita = palabrita.strip().lower() #Quita los enters y lo pone en minuscula
            sacar_imagenes(palabrita,params.num)
        else:#Marcar error por falta de diccioario
            logging.error("No se tiene el diccionario para generar palabras random, favor de descargar en esta carpeta ",diccionario)
    else:#Sacar imagen no random
        sacar_imagenes(params.prompt,params.num)
