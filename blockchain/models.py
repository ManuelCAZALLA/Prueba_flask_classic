import requests
from config import apikey
import sqlite3


class conecSqlite :
     def __init__(self, ruta):
        self.ruta = ruta

     def consultaSqlite(self, consulta):
            conexion = sqlite3.connect(self.ruta)
            cursor = conexion.cursor()
            cursor.execute(consulta)

            self.movimientos = []
            nombres_columnas = []

            for desc_columna in cursor.description:
                nombres_columnas.append(desc_columna[0])

            datos = cursor.fetchall()
            for dato in datos:
                movimiento = {}
                indice = 0
                for nombre in nombres_columnas:
                    movimiento[nombre] = dato[indice]
                    indice += 1
                self.movimientos.append(movimiento)
            conexion.close()

            return self.movimientos



class APIError(Exception):
    def __init__(self, code):
        if code == 400:
            msg = "Algo ha fallado en su consulta, vuelva a intentarlo más tarde."
        elif code == 401:
            msg = "Sin autorización -- Revise si su API KEY es correcta."
        elif code == 403:
            msg = "No tienes suficientes privilegios para realizar la consulta."
        elif code == 429:
            msg = "Ha excedido el número de consultas para su API KEY. Póngase en contacto en www.coinapi.io."
        elif code == 550:
            msg = "No hay información para la consulta realizada. Revise la configuración e inténtelo más tarde."
        else:
            msg = "Ha ocurrido un error. Por favor revise su conexión a Internet e inténtelo de nuevo mas tarde."
        super().__init__(msg)

class Consulta_monedas :
    def __init__(self) :
        self.digitales = []
        self.reales = []
       
        
    def conseguir_monedas(self,apikey):
            r = requests.get (f"https://rest.coinapi.io/v1/assets/?apikey={apikey}")

            if r.status_code != 200 :
                raise Exception ("Error en la consulta de criptomonedas :{}".format(r.status_code))
           
            lista_general = r.json()
            for item in lista_general :
                if item["type_is_crypto"] == 1:
                  self.digitales.append(item['asset_id'])
                else:
                    self.reales.append(item['asset_id'])
                    
class Cambio :
    def __init__(self,mon_digital) :
       
        self.mon_digital = mon_digital
        self.rate = None
        self.time = None
    
    def actualizar_cambio (self,apikey) :
     r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{self.mon_digital}/EUR?apikey={apikey}")
     resultado = r.json()  
     if r.status_code == 200:
        self.rate = resultado ['rate'] 
        self.time = resultado ['time'] 
     else:
         raise APIError(r.status_code)