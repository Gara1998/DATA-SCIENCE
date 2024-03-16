from funciones import *
import os

os.chdir(os.path.dirname(os.path.abspath('__file__')))
os.makedirs('data',exist_ok=True)

var='G'
offset=0
respuesta_json=llamada_api(offset,var)

df=json_to_df(respuesta_json)

while respuesta_json['data']['count']==100:
    offset=offset+100
    respuesta_json=llamada_api(offset,var)
    df_new=json_to_df(respuesta_json)
    df=pd.concat([df,df_new])

df.to_csv("data/df_marvel_test_"+ var +".csv", index=False)