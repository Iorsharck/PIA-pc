#pip install TAGS, Pillow, image, exif, ExifImage
from PIL.ExifTags import TAGS
from PIL import Image
from exif import Image as ExifImage
import os
import os.path
import logging
logging.basicConfig(filename='metadatos_imag.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)

#funcion que abre la imagen que utilizaremos para el codigo


def imprimir_metadatos(imagen_imprimir):
    imagen = Image.open(imagen_imprimir) #abre la imagen
    #obtiene los metadatos
    metadatos = imagen._getexif()
    if metadatos:
        try:
            with open( "reporte_metadatos.txt", 'a') as f:
                f.write("--------Metadatos de la imagen-----\n")
                for key, valor in metadatos.items():
                    nombre = TAGS.get(key, key)
                    print(f"{nombre}: {valor}")
                    f.write(f"{nombre}: {valor}\n")
        except:
            logging.info(f'algo salio mal con la imagen')
            logging.warning('intenta de nuevo con otra imagen')
    else:
        with open( "reporte.txt", 'a') as f:
            f.write("--------Metadatos de la imagen-----\n")
            print("La imagen no tiene metadatos.")
            f.write("Esta imagen no tiene metadatos EXIF\n")

# imrpimimos primero los metadatos de la imagen original


def metadatos_originales(imagen_path):
    try:
        print("Metadatos originales:")
        imprimir_metadatos(imagen_path)
    except Exception as e:
        logging.error("no se encontro una imagen",e)
        logging.info(f"ocurrio un error al meter la imagen")

# borramos los metadatos de la imagen para despues itruducir el mensaje


def borrar_metadatos(imagen):
    imagen_o = Image.open(imagen)
    imagen_o.info.update()
    imagen_o.save("imagen_bonita.jpg")


# introducimos el mensaje en los metadatos exif de la imagen


def meter_metadatos(msg1, msg2):
    image_modi = "imagen_bonita.jpg"
    try:
        with open(image_modi, "rb") as input_file:
            exif_img = ExifImage(input_file)
            exif_img.artist = msg1
            exif_img.copyright = msg2
    except Exception as e:
        logging.error(f"fallo algo al modifcar la imagen {e}")
        print("fallo algo al modifcar la imagen")

    try:
        with open(image_modi, "wb") as ofile:
            ofile.write(exif_img.get_file())
    except Exception as e:
        logging.info("no encontro la imagen modificada")
        print("no encontro la imagen modificada")

#imprimimos los metadatos modificados


def imprimir_metasmodi(image_modi):
    print("\nMetadatos modificados:")
    imprimir_metadatos(image_modi)

#ruta de la imagen


def meta():
    imgs = []
    ruta = 'C:/Users/mennd/OneDrive/Escritorio/PIA_PCPC/NUEVOS'
    valid_images = ".jpg"
    for f in os.listdir(ruta):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(os.path.join(ruta,f))
    if len(imgs) != 0:
        for name in imgs:
            metadatos_originales(name)
            borrar_metadatos(name)
            print("se borraror correctamente los metadatos")
    else:
        print("no se encontraron imagenes")
        logging.info('la carpeta no tiene imagenes, poner imagenes')
    


if __name__=='__main__':
    meta()
    print("se ejecuto correctamente")
