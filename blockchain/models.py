import requests
from config import apikey,ORIGIN_DATA
import sqlite3


class conecSqlite :
     def __init__(self,ORIGIN_DATA):
        self.ruta = ORIGIN_DATA

     def consultaSqlite(self,consulta):
            con = sqlite3.connect(self.ruta)
            cur = con.cursor()
            cur.execute(consulta)

            resultado = []
            columnas = cur.description


            filas = cur.fetchall()
            for dato in filas:
                movimiento = {}
                posicion = 0
                
                for nombre in columnas:
                    movimiento[nombre[0]] = dato[posicion]
                    posicion += 1
                resultado.append(movimiento)
            con.close()

            return resultado
    
    
     def consultaConParametros(self, consulta, params):
        con = sqlite3.connect(self.ruta)
        cur = con.cursor()
        resultado = False
        try:
            cur.execute(consulta, params)
            con.commit()
            resultado = True
        except Exception as error:
            print("ERROR SQLITE:", error)
            con.rollback()
        con.close()

        return resultado

     def consultar_saldo(self, consulta):
        con = sqlite3.connect(self.ruta)
        cur = con.cursor()
        cur.execute(consulta)
        datos = cur.fetchone()
        con.commit()
        con.close()
        return datos

     def total_euros_invertidos(self, consulta):
        con = sqlite3.connect(self.ruta)
        cur = con.cursor()
        cur.execute(consulta)
        datos = cur.fetchall()
        con.commit()
        con.close()
        return datos

     def calcular_saldo(self, monedas):
        consulta_compras = "SELECT sum(cantidad_to) FROM movimientos WHERE moneda_to = '" + \
            monedas + "'"
        consulta_ventas = "SELECT sum(cantidad_from) FROM movimientos WHERE moneda_from = '" + \
            monedas + "'"

        datos_compras = self.consultar_saldo(consulta_compras)
        datos_ventas = self.consultar_saldo(consulta_ventas)
        if datos_ventas[0] == None and datos_compras[0] == None:
            return 0
        elif datos_ventas[0] == None:
            return datos_compras[0]
        elif datos_compras[0] == None:
            return 0
        else:
            return datos_compras[0] - datos_ventas[0]



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
    def __init__(self,origen,destino) :
        self.moneda_from = origen
        self.moneda_to = destino
        self.cambio = 0.0
        
       
        
    def consulta_cambio(self):
        headers = {
            "X-CoinAPI-Key": apikey
        }
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_from}/{self.moneda_to}"
        respuesta = requests.get(url, headers=headers)

        if respuesta.status_code == 200:
            self.cambio = respuesta.json()["rate"]
            return(self.cambio)

        else:
            raise APIError(respuesta.status_code)
                    

     
def consulta_saldo(crypto):
        cryptosMonedas = {}
        conn= sqlite3.connect(ORIGIN_DATA)
        cur = conn.cursor()
        for moneda in crypto:
            consulta = f"SELECT ((SELECT (case when (SUM(cantidad_to)) is null then 0 else SUM(cantidad_to) end) as tot FROM movimientos WHERE moneda_to = '{moneda}') - (SELECT (case when (SUM(cantidad_from)) is null then 0 else SUM(cantidad_from) end) as ee FROM movimientos WHERE moneda_from = '{moneda}')) AS {moneda}"
            cur.execute(consulta)
            fila =cur.fetchall() 
            cryptosMonedas[moneda] = fila[0][0]  
        conn.close()
    
        return cryptosMonedas 
    
def consulta_valor():    
        total = 0
        monedas_disponibles = ["BTC", "EUR", "ETH", "XRP", "SOL","BNB","ADA","DOT","USDT","MATIC"]
        monederoActual = consulta_saldo(monedas_disponibles)
        url = requests.get(f"https://rest.coinapi.io/v1/exchangerate/EUR?&apikey={apikey}")
        
        if url.status_code != 200:
            raise APIError(url.status_code)
        
        resultado = url.json()

        for i in monederoActual.keys():
            for e in resultado['rates']:
                if e['asset_id_quote'] == i:
                    total += 1/e['rate'] * monederoActual[i]
                    
        return total 