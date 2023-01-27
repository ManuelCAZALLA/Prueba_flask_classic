from blockchain import app
from flask import render_template,request, redirect, url_for, flash
from blockchain.models import *
from blockchain.forms import MovementForm
from datetime import date,datetime



RUTA = "data/movimientos.sqlite"

@app.route("/")
def index():
    try:
        sqlite = conecSqlite(RUTA)
        movimientos = sqlite.consultaSqlite("SELECT * FROM movimientos.sqlite ORDER BY date")
        return render_template("index.html",movements = movimientos, puntero = "index.html")
        
    except:
        flash("Base de datos no disponible,intentelo más tarde por favor",
              category="fallo")
    return render_template("index.html")

'''@app.route("/purchase",methods =["GET","POST"])
def comprar ()'''
