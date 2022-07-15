#Importamos las librerías necesarias 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
baseDatos = myclient["base_RG_Juego"] # en esta variable creamos la base de datos
#Retorna la lista del sistema de la base de datos 
print(myclient.list_database_names())

#Verificamos que la base de datos exista
dblist = myclient.list_database_names()
if "base_RG_Juego" in dblist:
    print("La base de datos existe")
else:
    print("La base de datos no existe")

#consultamos los datos que se encuentran en la base de datos creada 
datosjuego = baseDatos["datosJuego"]

#condicion que nos permite encontrar los datos en la colección datosJuego
for datos in datosjuego.find():
  print(datos)
