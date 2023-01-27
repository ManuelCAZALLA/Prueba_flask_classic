from flask import Flask

app = Flask (__name__,instance_relative_config=True) # con esto inicio
app.config.from_object("config") # esto reconoce la clave secretra desde config.py

from blockchain.routes import * # aqui importo todas la rutas que defina en routes. Lo tengo que poner debajo de app
