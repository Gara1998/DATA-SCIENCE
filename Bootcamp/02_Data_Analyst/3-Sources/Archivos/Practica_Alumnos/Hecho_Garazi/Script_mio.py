import os
import shutil

def crear_carpetas():
    os.makedirs('Imagenes', exist_ok=True)
    os.makedirs('Documentos', exist_ok=True)
    os.makedirs('Softwares', exist_ok=True)
    os.makedirs('Audios', exist_ok=True)
    os.makedirs('Archivos_comprimidos', exist_ok=True)
    os.makedirs('Otros', exist_ok=True)
    
def mover_archivos():
    
    #Variables
    doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx') 
    img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff') 
    audios_types= ('.mp4','.mp3')
    comprimidos=('.zip','.rar')
    software_types = ('.exe', '.pkg', '.dmg') 
    
    
    for archivo in os.listdir():
        if os.path.isdir(archivo):
            os.makedirs('Carpetas', exist_ok=True)
            shutil.move(archivo,'Carpetas') 
        else:
            crear_carpetas()
            if archivo.endswith(img_types):
                shutil.move(archivo,'Imagenes')
            elif archivo.endswith(doc_types):
                shutil.move(archivo,'Documentos')
            elif archivo.endswith(software_types):
                shutil.move(archivo,'Softwares')
            elif archivo.endswith(audios_types):
                shutil.move(archivo,'Audios')
            elif archivo.endswith(comprimidos):
                shutil.move(archivo,'Archivos_comprimidos')
            else:
                shutil.move(archivo,'otros')
            
def programa_principal(direccion):
    os.chdir(direccion)
    mover_archivos()
    
ruta='/Users/Garazi/Downloads'
programa_principal(ruta)