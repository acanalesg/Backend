# import necessary modules
import json
import sys
import mysql.connector
import time
import os

# define a new variable for tweets
tweets=[]
global contador

fecha = time.strftime('%Y%m%d_%H%M%S')

config_mysql = {
    'user': 'upsa',
    'password': '12345',
    'host': 'localhost',
    'database': 'pruebaTwitter',
}


def unescape(s):
    s = s.replace("'", "&apos;")
    s = s.replace(", '", "&coma;")
    s = s.replace("\\", "&barra;")
    return s


# conectamos al servidor MySql
conector = mysql.connector.connect(**config_mysql)

cursor = conector.cursor()

#save_file = open('datos.json', 'a')


datos = open('datos.json')
datos_fecha = open('datos'+ fecha +'.json',"w")

for line in open('datos.json'):
    try:
        tweets.append(json.loads(line))
        datos_fecha.write(line)
    except:
        pass


tweet=tweets[0]

contador = 0

for tweet in tweets:

    print "-----------------------------------------"

    #Comprobacion id
    if 'id' not in tweet:
        id_tweet = None
    else:
        id_tweet = tweet['id']
        print "Id tweet: " + str(id_tweet)

    #Comprobacion usuario
    if 'user' not in tweet:
            usuario = None
    else:
        if 'screen_name' not in tweet['user']:
            usuario = None
        else:
            usuario = tweet['user']['screen_name']
            print "Usuario: " + str(usuario)


    #Comprobacion creado
    if 'created_at' not in tweet:
        creado = None
    else:
        creado = tweet['created_at']
        print "Creado: " + str(creado)

    #Comprobacion texto
    if 'text' not in tweet:
        texto = None
    else:
        texto = tweet['text']
        print "Texto: " + texto
        texto = unescape(texto)

    #Comprobacion idioma
    if 'lang' not in tweet:
        idioma = None
    else:
        idioma = tweet['lang']
        print "Idioma: " + str(idioma)

    #Comprobacion codigo pais
    if 'place' not in tweet:
        codigo_pais = "NULL"
    elif tweet['place'] == None:
        codigo_pais = None
    else:
        if 'country_code' not in tweet['place']:
            codigo_pais = "NULL"
        else:
            codigo_pais = tweet['place']['country_code']
            print "Codigo Pais: " + str(codigo_pais)



    #Comprobacion de la geolocalizacion

    if 'geo' not in tweet:
        latitud = "NULL"
        longitud = "NULL"
    elif tweet['geo'] == None:
        latitud = None
        longitud = None
    else:
        if 'coordinates' not in tweet['geo']:
            latitud = None
            longitud = None
        else:
            latitud = tweet['geo']['coordinates'][0]
            longitud = tweet['geo']['coordinates'][1]
            print "Coordenadas: Latitud: " + str(latitud) + " Longitud: " + str(longitud)



    #Comprobacion de la localizacion

    if 'user' not in tweet:
            localizacion = None
    else:
        if 'location' not in tweet['user']:
            localizacion = "NULL"
        else:
            localizacion = tweet['user']['location']
            print "Localizacion: " + localizacion
            localizacion = unescape(localizacion)



    contador += 1
    print "Contador:" + str(contador)



    query = """INSERT INTO tweets (id_tweet, nombre_usuario, creado, texto, latitud, longitud, localizacion ,codigo_pais, idioma) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (id_tweet,usuario,creado,texto,latitud,longitud,localizacion, codigo_pais,idioma)
    print query
    cursor.execute(query)
    conector.commit()

#esta parte da fallo al final, intento borrar lo de dentro de datos.json
archivo = open("datos.json","rw+")

lineas = archivo.readlines()

for linea in lineas:
    #lineas.remove(linea)
    pass

archivo.truncate(0)
archivo.close()


