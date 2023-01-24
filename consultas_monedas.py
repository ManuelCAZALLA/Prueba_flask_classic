import requests

apikey = "A944BA45-DDE6-427C-AB87-A3C2ED4C0344"
moneda_cripto = input("Ingrese una Criptomoneda: ").upper()
while moneda_cripto != "" and moneda_cripto.isalpha(): # no realizar consulta si el input esta vacio
    

    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}")

    r.status_code # esto me dice el codigo de peticion , 200 es bueno

    r.text # aqui me muestra los datos de la consulta , time, monedas y el cambio

    resultado = r.json() # guardo el r.json en resultado

    # si es correcto me imprime el resultado, si no me imprime el error
    if r.status_code == 200 :
        print("{:.2f} €".format(resultado['rate']))
    else :
        print (resultado ['error'])
        
    moneda_cripto = input("Ingrese una Criptomoneda: ").upper() # vuelvo a pedir que ingrese cripto
       
        

   
        
