# App blockchain de criptomonedas

Programa hecho en python para la compra - venta de criptomonedas desde www.coinapi.io.

# Instalacion

- Obtener la apikey siguiendo los pasos en www.coinapi.py
- Renombrar el fichero 'config_template.py' a 'config.py' y 
poner su apikey.

````
apikey = "774747848hhfhf"
````
### Instalacion de dependencias
- Dentro de su entorno ejecutar el comando :
```
pip install -r requirements.txt
```
- Las librerias utilizadas son request,pytest y flask
## Base de datos
- Crear base de datos movimientos utilizando movimientos_create que se encuentra en el directorio data.