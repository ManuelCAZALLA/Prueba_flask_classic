from blockchain import app
from flask import render_template,request, redirect, url_for, flash
from blockchain.models import *
from blockchain.forms import MovementForm
from datetime import date,datetime
from config import *





@app.route("/")
def index():
    try:
        sqlite = conecSqlite(ORIGIN_DATA)
        movimientos = sqlite.consultaSqlite("SELECT * from movimientos")
        return render_template("index.html",movements=  movimientos, puntero = "index.html",pageTitle ="movimimentos")
        
    except:
        flash("Base de datos no disponible,intentelo más tarde por favor",
              category="fallo")
        return render_template("index.html")



@app.route("/purchase",methods =["GET","POST"])
def comprar ():
    if request.method == "GET":
        form = MovementForm()
        return render_template("purchase.html", form=form, puntero="purchase.html")
    else:
        try:
            form = MovementForm(data=request.form)

            moneda_from = form.moneda_from.data
            moneda_to = form.moneda_to.data
            cantidad_from = form.cantidad_from.data
            cantidad_from = float(round(cantidad_from,8))

            convertir = Consulta_monedas(moneda_from, moneda_to)
            PU = convertir.consulta_cambio()
            PU = float(round(PU,8))
            cantidad_to = cantidad_from * PU
            cantidad_to = float(round(cantidad_to,8))

            saldo = conecSqlite(ORIGIN_DATA).calcular_saldo(moneda_from)
            if moneda_from != "EUR" and saldo < float(cantidad_from):
                flash(f"No tienes suficientes monedas {moneda_from} ")
                return render_template("purchase.html", form=form)
                
            if form.consultar.data:
                return render_template("purchase.html", form=form, cantidad_to=cantidad_to, PU=PU)

        except APIError as err:
            flash(err)
            return render_template("purchase.html", form=form)

        if form.aceptar.data:
            if form.validate():
                form = MovementForm(data=request.form)
                sqlite = conecSqlite(ORIGIN_DATA)
                consulta = "INSERT INTO movimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)"
                moneda_from = str(form.moneda_from.data)
                moneda_to = str(form.moneda_to.data)
                cantidad_from = float(cantidad_from)
                form.fecha.data = date.today()
                fecha = form.fecha.data
                form.hora.data = datetime.today().strftime("%H:%M:%S")
                hora = form.hora.data
                params = (fecha, hora, moneda_from,
                          cantidad_from, moneda_to, cantidad_to)
                resultado = sqlite.consultaConParametros(consulta, params)

                if resultado:
                    flash("Movimiento actualizado correctamente", category="exito")
                    return redirect(url_for("index"))

                else:
                    return render_template("purchase.html", form=form, cantidad_to=cantidad_to, errores=["Algo ha fallado con la conexión en la Base de datos"])

            else:
                return render_template("purchase.html", form=form, cantidad_to=cantidad_to, errores=["Algo ha fallado en la validación de  los datos"])

        else:
            return redirect(url_for("comprar"))
        
@app.route("/status",methods = ["GET","POST"])
def estado():
    
    return ("Esto es el estado")

  

