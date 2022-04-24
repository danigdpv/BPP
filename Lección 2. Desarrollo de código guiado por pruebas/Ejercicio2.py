import pytest
import Ejercicio1 as l1
import pandas as pd

def test_suma():
    df = l1.lectura_fichero()
    df = l1.comp_cont(df)    
    assert isinstance(l1.suma(df),pd.core.series.Series) == True

def test_gasto():
    df = l1.lectura_fichero()
    df = l1.comp_cont(df) 
    assert l1.gasto(l1.suma(df)) == 'Abril'


def test_ahorro():
    df = l1.lectura_fichero()
    df = l1.comp_cont(df)    
    assert l1.ahorro(l1.suma(df)) == 'Enero'

def test_media():
    df = l1.lectura_fichero()
    df = l1.comp_cont(df)
    assert float(l1.media(l1.suma(df))) == -1319.1666259765625    


def test_sumgastos():
    df = l1.lectura_fichero()
    df = l1.comp_cont(df)    
    assert l1.sumgastos(l1.suma(df)) == -51106.0

def test_sumahorros():
    df = l1.lectura_fichero()
    df = l1.comp_cont(df)
    assert l1.sumahorros(l1.suma(df)) == 35276.0    


