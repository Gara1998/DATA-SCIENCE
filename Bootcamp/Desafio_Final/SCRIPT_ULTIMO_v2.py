#Librerias necesarias
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#Funciones para transponer tablas
def tabla_usuarios(tabla):
    df=tabla.pivot_table(index='Id_Usuario', columns='Id_categoria', values='Nivel')
    df=df.fillna(0)
    return df

def tabla_ofertas(tabla):
    df=tabla.pivot_table(index='Id_offer', columns='Id_categoria', values='Nivel')
    df=df.fillna(0)
    return df

#Funciones para que la estructura de ambas tablas sea la misma
#Tabla de usuarios: completar_tablas(df_usuarios, df_ofertas) 
#Tabla de ofertas: completar_tablas(df_ofertas, df_usuarios)
def completar_tablas(tabla1,tabla2):
    caracteristicas_1 = tabla1.keys()
    caracteristicas_2 = tabla2.keys()
    columnas_faltantes=list(set(caracteristicas_2) - set(caracteristicas_1))
    df_faltantes=pd.DataFrame(0, index=tabla1.index, columns=columnas_faltantes)
    df_final=pd.concat([tabla1,df_faltantes],axis=1).sort_index(axis=1)
    return df_final

#Funcion para dar distintos pesos a los estudios y a las habilidades/idiomas
def pesos(tabla):
    columnas_estudios = [col for col in tabla.columns if not col.startswith('HAB') and not col.startswith('IDIOMA')]
    columnas_idiomas= [col for col in tabla.columns if  col.startswith('IDIOMA')]
    columnas_habilidades= [col for col in tabla.columns if  col.startswith('HAB')]
    tabla[columnas_estudios]=tabla[columnas_estudios]*0.85
    tabla[columnas_idiomas]=tabla[columnas_idiomas]*0.1
    tabla[columnas_habilidades]=tabla[columnas_habilidades]*0.05
    return tabla


usuarios=pd.read_csv('Tabla_perfiles.csv')
ofertas=pd.read_csv('Tabla_ofertas.csv')
df_usuarios=tabla_usuarios(usuarios)
df_ofertas=tabla_ofertas(ofertas)
df_usuarios_final=completar_tablas(df_usuarios, df_ofertas) 
df_ofertas_final=completar_tablas(df_ofertas, df_usuarios)
df_ofertas_final=pesos(df_ofertas_final)
df_usuarios_final=pesos(df_usuarios_final)


# Calcula la similitud del coseno entre los estudiantes y las ofertas
similitud_cos = cosine_similarity(df_usuarios_final,df_ofertas_final)
df_similitud_cos = pd.DataFrame(similitud_cos, index=df_usuarios_final.index, columns=df_ofertas_final.index)

#Crear archivos para cada usuario, que guarda el valor de relacion que tiene cada oferta.
for i in range(len(df_similitud_cos)):
    nombre_archivo=df_similitud_cos.iloc[i].name
    serie_filtrada=df_similitud_cos.iloc[i].sort_values(ascending=False)
    contenido_archivo=serie_filtrada[serie_filtrada > 0.75]
    contenido_archivo.to_csv(nombre_archivo + '.csv', header=False)

#Crear archivos para cada oferta, que guarda el valor de relacion que tiene cada usuario.
for j in range(len(df_similitud_cos)):
    nombre_archivo=df_similitud_cos.iloc[:, j].name
    serie_filtrada=df_similitud_cos.iloc[:, j].sort_values(ascending=False)
    contenido_archivo=serie_filtrada[serie_filtrada > 0.75]
    contenido_archivo.to_csv(nombre_archivo + '.csv', header=False)
