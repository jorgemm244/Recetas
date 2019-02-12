import pickle



def guardar_datos(datos, archivo_origen):
    archivo = open(archivo_origen+'.dat', 'wb')
    pickle.dump(datos, archivo)
    archivo.close()
    return True

def recuperar_datos(archivo_origen):
   archivo = open(archivo_origen+".dat", "rb")
   archivo_leido = pickle.load(archivo)
   return archivo_leido

