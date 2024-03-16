import os
import shutil

class Fichero:

    def __init__(self, carpeta, extensions, carpeta_ordenar, ruta=None):
        self.carpeta = carpeta
        self.extensions = extensions
        self.carpeta_ordenar = carpeta_ordenar
        self.ruta = ruta
        self.select_dir()
        self.create_dir()
        self.move_file()

    def select_dir(self):
        if self.ruta:
            self.ruta = os.path.join(self.ruta, self.carpeta_ordenar)
        else:
            self.ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.carpeta_ordenar)
        os.chdir(self.ruta)

    def create_dir(self):
        os.makedirs(self.carpeta, exist_ok=True)

    def move_file(self):
        for archivo in os.listdir():
            if os.path.isdir(archivo):
                print(archivo, "es una carpeta")
            elif self.extensions==None:
                shutil.move(archivo, self.carpeta)
            elif archivo.endswith(self.extensions):
                shutil.move(archivo, self.carpeta)
