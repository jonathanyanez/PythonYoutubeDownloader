#/usr/bin/env python3
import youtube_dl
import sys

"""
Se usa la libreria youtube_dl
"""

print("¿Qué desea realizar?:")
print("1. Descarga unitaria")
print("2. Descarga de lista")
print("3. Descarga desde archivo")
opcion=input("$>")

options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',}],
    }

if(opcion=="1"):
    url=input("Direccion URL: ")
    with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])

elif(opcion=="2"):
    url=input("Introduce la URL del primer elemento de la lista: ")
    with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])
elif(opcion=="3"):
    archivo=input("Ruta del archivo: ")
    with open(archivo, 'r') as f:
        for linea in f:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([linea])
    f.close()
else:
    print("La opcion que ha indicado no esta disponible\n")

sys.exit(0)