from blockchain.models import *
from config import apikey

def test_consulta_monedas ():
    conseguir = Consulta_monedas()
    assert isinstance (conseguir,Consulta_monedas)
    conseguir.conseguir_monedas(apikey)
    assert len(conseguir.digitales)==16156
    assert len(conseguir.reales)== 222
    
def test_cambio():
    cambio = Cambio("BTC")
    assert cambio.rate == None
    assert cambio.time == None
    cambio.actualizar_cambio(apikey) 
    assert cambio.rate > 0
    assert isinstance(cambio.time,str) 
    
def test_cambio_error():
    error = Cambio("ggg")
    error.actualizar_cambio(apikey)     