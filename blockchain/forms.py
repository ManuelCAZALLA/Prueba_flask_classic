from flask_wtf import FlaskForm
from wtforms import HiddenField,DateField,TimeField,SelectField,FloatField,SubmitField
from wtforms.validators import DataRequired,ValidationError,NumberRange

monedas_disponibles = ["BTC", "EUR", "ETH", "XRP", "SOL","BNB","ADA","DOT","USDT","MATIC"]

def validate_monedas_diferentes(form,field):
      if field.data == form.moneda_from.data:
         raise ValidationError(message="Debes elegir monedas diferentes")  



class MovementForm(FlaskForm):
    id = HiddenField()
    fecha = DateField("Fecha")
    hora = TimeField("Hora")

    moneda_from = SelectField("From",choices=[
        ("EUR","EUR"), ("BTC","BTC"), ("ETH","ETH"), ("XRP","XRP"), ("SOL","SOL"),("BNB","BNB"),("ADA","ADA"),("DOT","DOT"),("USDT","USDT"),("MATIC","MATIC")], validators=[DataRequired()])
    moneda_to = SelectField("To", choices=[
        ("EUR","EUR"), ("BTC","BTC"), ("ETH","ETH"), ("XRP","XRP"), ("SOL","SOL"),("BNB","BNB"),("DOT","DOT"),("USDT","USDT"),("MATIC","MATIC")], validators=[DataRequired(),validate_monedas_diferentes])
    
 
    cantidad_from = FloatField("Q:",validators=[DataRequired(message="La cantidad debe de ser un número positivo y mayor que 0"),NumberRange(min= 0.1,max= 99999999)])
    
    
    consultar = SubmitField("calculate")
    borrar = SubmitField("backspace")
    aceptar = SubmitField("done")
    
      
    
   