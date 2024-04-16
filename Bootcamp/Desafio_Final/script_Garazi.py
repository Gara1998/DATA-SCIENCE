#Librerias necesarias
import numpy as np
import pandas as pd

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


#Escojiendo un usuario nos devuelve las ofertas donde coinciden dos o mas habilidades
def recomendaciones(usuario):
    usuarios=pd.read_csv('Tabla_perfiles.csv')
    ofertas=pd.read_csv('Tabla_ofertas.csv')

    df_usuarios=tabla_usuarios(usuarios)
    df_ofertas=tabla_ofertas(ofertas)
    df_usuarios_final=completar_tablas(df_usuarios, df_ofertas) 
    df_ofertas_final=completar_tablas(df_ofertas, df_usuarios)

    lista_ofertas=[]
    for j in range(len(df_ofertas_final)):
        oferta_j = df_ofertas_final.iloc[j]
        contador=0
        for i in usuario.index:
            if (oferta_j.index == i).any() and oferta_j[i] != 0 and usuario[i]!=0:
                contador += 1
        if contador>4:  #menos de 4 coincidencias no es una recomendación muy buena. Hay que crear usuarios y ofertas parecidas.
            lista_ofertas.append(oferta_j.name)
    print(lista_ofertas)

#a las ofertas se le recomiendan usuarios
def recomendacion_usuario(oferta):
    usuarios=pd.read_csv('Tabla_perfiles.csv')
    ofertas=pd.read_csv('Tabla_ofertas.csv')

    df_usuarios=tabla_usuarios(usuarios)
    df_ofertas=tabla_ofertas(ofertas)
    df_usuarios_final=completar_tablas(df_usuarios, df_ofertas) 
    df_ofertas_final=completar_tablas(df_ofertas, df_usuarios)
    lista_usuarios=[]

    for j in range(len(df_usuarios_final)):
        usuario_j = df_usuarios_final.iloc[j]
        contador=0
        for i in oferta.index:
            if (usuario_j.index == i).any() and usuario_j[i] != 0 and oferta[i]!=0:
                contador += 1
        if contador>4:
            lista_usuarios.append(usuario_j.name)
    print(lista_usuarios)
        

#def empresa_o_usuario(name): hacer una funcion que escoja si es una empresa o un usuario.
   #si es oferta  --> ejecutamos la funcion recomendacion_usuario
   #si es usuario --> ejecutamos la funcion recomendaciones


#Prueba con un unico usuario:
usuarios=pd.read_csv('Tabla_perfiles.csv')
ofertas=pd.read_csv('Tabla_ofertas.csv')
df_usuarios=tabla_usuarios(usuarios)
df_ofertas=tabla_ofertas(ofertas)
df_usuarios_final=completar_tablas(df_usuarios, df_ofertas) 
df_ofertas_final=completar_tablas(df_ofertas, df_usuarios)
recomendaciones(df_usuarios_final.iloc[0])

