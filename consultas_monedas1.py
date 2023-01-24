import requests
from config import apikey
 
r = requests.get (f"https://rest.coinapi.io/v1/assets/?apikey={apikey}")

if r.status_code != 200 :
    raise Exception ("Error en la consulta de criptomonedas :{}".format(r.status_code))

lista_general = r.json()
lista_criptos =[]

for item in lista_general :
    if item["type is cripto"] == 1:
        lista_criptos.append(item['asset_id'])
        
print ("Moneda digital:",len (lista_criptos))
print ("Moneda no digital:",len (lista_general) - len(lista_criptos))          

moneda_cripto = input("Ingrese una Criptomoneda: ").upper()
while moneda_cripto != "" and moneda_cripto.isalpha(): 
    if moneda_cripto in lista_criptos :
        
        r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}")

        resultado = r.json() 

    
    if r.status_code == 200 :
        print("{:.2f} €".format(resultado['rate']))
    else :
        print (resultado ['error'])
        
    moneda_cripto = input("Ingrese una Criptomoneda: ").upper() 
        

   
        
