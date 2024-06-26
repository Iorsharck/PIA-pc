import os 
from PIL.ExifTags import TAGS
from PIL import Image
import os.path
import logging
import requests
import os
import bs4
import sys
import argparse

parser = argparse.ArgumentParser(description='Saca todas las imagenes de una pagina web')
parser.add_argument('--web', type=str, help='Pagina web', default=
                    "https://www.wired.com/2012/12/oops-did-vice-just-give-away-john-mcafees-location-with-this-photo/")
args = parser.parse_args()

#aqui esta donde se guardan los logging
logging.basicConfig(filename='webscrappy_imag.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

#aqui se comprueba que este bien escrito la url con http://
def cheacador(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "http://" + url

#aqui se verifica que tenga html la pagina web
def verifica_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            if soup.find('html'):
                print("La página tiene contenido HTML")
            else:
                print("La página no tiene contenido HTML, intente con otra pagina")
                sys.exit()
        else:
            print("No se pudo acceder a la página:", response.status_code)
            sys.exit()
    except Exception as e:
        print("intente de nuevo, ocurrio un error con url")
        logging.info(f"Ocurrió un error:", e)
        sys.exit()
 
#aqui se hace un llamado a la pagian y se saca los datos html
def conexion_request(url_nueva):
    os.makedirs('imagen_segura', exist_ok=True)
    print('esperando la pagina %s...' % url_nueva)
    res = requests.get(url_nueva)
    soup = bs4.BeautifulSoup(res.text, "html.parser")  #aqui se lee el html y se parsea
    
    imagenes = soup.find_all('img') #buscan en todo html las imgenes
    if imagenes == []:
        print('No se encontró imagenes en html.')
    else:
        for img in imagenes:
            imgUrl = img.get('src')
            try:
                if imgUrl.startswith("http"):
                    print('Descargando %s...' % (imgUrl))
                    response = requests.get(imgUrl)
                    if response.status_code == 200:      #aqui se descargan las imagenes y se meten a la carpeta
                        imageFile = open(os.path.join('imagen_segura', os.path.basename(imgUrl)),'wb')
                        for chunk in response.iter_content(100000):
                            imageFile.write(chunk)
                            imageFile.close()
                else:
                    print('Descargando %s...' % (imgUrl))
                    imgUrl = url_nueva + imgUrl
                    response = requests.get(imgUrl)
                    if response.status_code == 200:
                        imageFile = open(os.path.join('imagen_segura', os.path.basename(imgUrl)),'wb')
                        for chunk in response.iter_content(100000):
                            imageFile.write(chunk)
                            imageFile.close()
            except:
                logging.info(f"la imagen {imgUrl} ,no es compatible")

#se hace el proceso de impresion de los metadatos
def imprimir_metadatos(imagen_imprimir):
    imagen = Image.open(imagen_imprimir)
    metadatos = imagen._getexif()
    if metadatos:
         try:
              with open( "reporte_webscrapping.html", 'a') as f:
                   f.write("--------Metadatos de las imagenenes-----\n")
                   for key, valor in metadatos.items():
                        nombre = TAGS.get(key, key)
                        print(f"{nombre}: {valor}")
                        f.write(f"{nombre}: {valor}\n")
         except Exception as e:
              logging.info(f'algo salio mal con los reportes',e)
    else:
        with open( "reporte_webscrapping.html", 'a') as f:
            f.write("--------Metadatos de las imagenenes-----\n")
            print("La imagen no tiene metadatos.")
            f.write("La imagen no tiene metadatos.\n")

#se imprime los metadatos 
def metadatos(imagen_path):
    try:
         imprimir_metadatos(imagen_path)
    except Exception as e:
        logging.info("ocurrio una error al meter la imagen")
        print("hubo un error al introducir la imagen")

#verifica que en la carpeta tenga imagenes 
def Meta():
    imgs = []
    ruta = os.getcwd()+'/imagen_segura'
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(ruta):
         ext = os.path.splitext(f)[1]
         if ext.lower() not in valid_images:
              continue
         imgs.append(os.path.join(ruta,f))
    if len(imgs) != 0:
        i=1
        for name in imgs:
            print("--------Metadatos de las imagenen ",i,"-----")
            metadatos(name)
            i=i+1
    else:
         print("no se encontraron imagenes")
         logging.info('la carpeta no contiene imagnes, se acabo la ejecucio')


def menu(url):
    verifica_html(url)
    url_nueva = cheacador(url)
    conexion_request(url_nueva)
    Meta()


if __name__=='__main__':
    menu(args.web)
