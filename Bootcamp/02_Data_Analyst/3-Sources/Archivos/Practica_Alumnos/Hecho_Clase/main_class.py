from clase import Fichero
from variables import *

ruta = "c:\\Users\\david\\TheBridge\\DT_PT_Sep2023\\02_Data_Analyst\\3-Sources\\Archivos\\Practica"

documentos = Fichero("Documentos", doc_types, "descargas_test", ruta)
imagenes = Fichero("Imagenes", img_types, "descargas_test", ruta)
softwares = Fichero("Software", software_types, "descargas_test", ruta)
otros = Fichero("Otros", None , "descargas_test", ruta)
# notebooks = Fichero("Notebook", notebooks_types , "descargas_test", ruta)
# music = Fichero("Music", music_types , "descargas_test", ruta)
# videos = Fichero("Video", video_types , "descargas_test", ruta)