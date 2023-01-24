from blockchain.models import *
from config import apikey

consultar = Consulta_monedas()
consultar.conseguir_monedas(apikey)

#print(f"La cantidad de criptos son {consultar.digitales} y las no criptos son {consultar.reales}")

cripto = input ("Ingrese criptomoneda: ").upper()

while cripto != "" and cripto.isalpha():
    if cripto in consultar.digitales:

        cambio = Cambio(cripto)
        try:
            cambio.actualizar_cambio(apikey)
            print ("{:,.2f}€".format (cambio.rate).replace(",","@").replace(".",",").replace("@","."))
        
        except APIError as error:
            print ( error)
          
        
        
        
        cripto = input ("Ingrese criptomoneda: ").upper()