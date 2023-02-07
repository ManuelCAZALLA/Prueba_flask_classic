# App blockchain de criptomonedas

Aplicacion web con la que podra simular la compra/venta de criptomonedas,registro de inversiones y el estado de nuestra inversion

# Instalacion
### 1. Crear y activar de entorno virtual :
- En windows python -m venv nombre del entorno virtual y en mac/linux python3 -m venv nombre del entorno virtual
-  Activar entorno en mac/linux : source/nombre del entorno virtual/bin/activate
- Activar en windows : nombre del entorno virtual\Scripts\activate

### 2. Instalar carpeta requierements.txt
 ````
pip install -r requierements.txt
````
### 3. Renombrar variables de entorno
#### Renombrar config_templates.py a config.py:
- apikey = " aqui su apikey"
- ORIGIN_DATA = "aqui su ruta a su base de datos"
#### Renombrar .venv_templates a .venv : 
- FLASK_APP = main.py
- FLASK_DEBUG = true

### 4. Obtener la apikey 
- Visite la pagina CoinApi para obtener su APIkey

poner su apikey.
### 5. Base de datos
- Crear base de datos "movimientos" utilizando movimientos_create que se encuentra en el directorio data.

# Ejecucion de App
### Ingrese en consola :
- export FLASK_APP=main.py
- flask run
- En caso de que el puerto 5000 este ocupado ingresar: flask --app main run -p 5001