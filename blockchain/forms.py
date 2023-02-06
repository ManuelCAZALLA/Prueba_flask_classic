from flask_wtf import FlaskForm
from wtforms import DateField,FloatField, SubmitField,TimeField,HiddenField,SelectField
from wtforms.validators import DataRequired,ValidationError,NumberRange

monedas_disponibles = ["BTC", "EUR", "ETH", "XRP", "SOL","BNB","ADA","DOT","USDT","MATIC"]

def validar_moneda(form,field):
        if field.data == form.moneda_from:
            raise ValidationError ("Debe elegir monedas diferentes")

class MovementForm(FlaskForm):
    id = HiddenField()
    fecha = DateField("Fecha")
    hora = TimeField("Hora")

    moneda_from = SelectField("From",choices=[
        ("EUR","EUR"), ("BTC","BTC"), ("ETH","ETH"), ("XRP","XRP"), ("SOL","SOL"),("BNB","BNB"),("ADA","ADA"),("DOT","DOT"),("USDT","USDT"),("MATIC","MATIC")], validators=[DataRequired()])
    moneda_to = SelectField("To", choices=[
        ("EUR","EUR"), ("BTC","BTC"), ("ETH","ETH"), ("XRP","XRP"), ("SOL","SOL"),("BNB","BNB"),("DOT","DOT"),("USDT","USDT"),("MATIC","MATIC")], validators=[DataRequired(), validar_moneda])
    
 
    cantidad_from = FloatField("Q:",validators=[DataRequired(message="La cantidad debe de ser un número positivo y mayor que 0"),
    NumberRange(min=0.00001, max=99999999)])
    
    

    consultar = SubmitField("calculate")

    borrar = SubmitField("backspace")
    aceptar = SubmitField("done")
    
    

    

