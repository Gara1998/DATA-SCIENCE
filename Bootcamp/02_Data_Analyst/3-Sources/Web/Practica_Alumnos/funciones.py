import hashlib
import requests
import datetime
import pandas as pd
from variables import *

#Esto no se que hace. Pone en la web de marvel que hay que hacerlo para trabajar con api
def hash_params(timestamp,priv_key,pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


def llamada_api(offset,letra): #ofset valor numerico. Es un valor numerico: le podemos indicar un numero de supereroes que no queremos que nos imprima
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') 

    pub_key = '9511d7388bac681f0627b1ad466a94ac'
    priv_key = 'fd3a98d3cb8cbd23e08035027ac6826a87c3a87e'

    params = {'ts': timestamp, 
            'apikey': pub_key, 
            'hash': hash_params(timestamp,priv_key,pub_key),
            'offset':offset,
            'nameStartsWith':letra,
            'limit': 100}

    url = 'http://gateway.marvel.com/v1/public/characters'
    res = requests.get(url,params=params)
    return res.json()


#La siguiente funcion pasa de json a dataframe
def json_to_df(respuesta_json):
    marvel_dict = {"id": [],
                "name":[],
                "picture_url":[]}

    for elem in respuesta_json['data']['results']:
        # print(elem['id'])
        marvel_dict['id'].append(elem.get('id'))
        # print(elem['name'])
        marvel_dict['name'].append(elem.get('name'))
        # print(elem['thumbnail'])
        pic_url = elem.get('thumbnail').get("path") + '.' + elem.get('thumbnail').get("extension")
        marvel_dict['picture_url'].append(pic_url)

    df= pd.DataFrame(marvel_dict)
    return df