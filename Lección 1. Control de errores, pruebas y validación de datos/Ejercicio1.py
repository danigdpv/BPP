import pandas as pd
import plotly.express as px

class ErrorIncompleto(Exception):
    pass

# Esta función gestiona la lectura del fichero y dará error si no lo puede leer cerrando el programa.
def lectura_fichero():
    try:
        df = pd.read_csv('finanzas2020.csv', sep='\t')
        return df
    except IOError:
        print("El fichero no existe o no se disponen de los permisos necesarios para leerlo")
        exit()

#Esta función comprueba que existan las 12 columnas de los 12 meses. Si no cerrará el programa.
def columnas(contenido):
    count =  len(contenido.columns)
    try:
        if count == 12:
            print("El Dataset contiene la información de los 12 meses del año")
    except ErrorIncompleto:
            print("El dataset está incompleto. No contiene información de los 12 meses del año")
            exit()

#Esta función comprueba que todos los valores son tipo float. Si hay un valor string lo transformará a numérico.
def comp_cont(contenido):
    try:
        contenido = contenido.astype(float)
    except ValueError:
        for col in contenido.columns:
            contenido[col] = pd.to_numeric(contenido[col],downcast='float', errors='coerce')
        print("Se han convertido los datos tipo texto a numéricos ya que había datos incorrectos")
        return contenido

def suma(contenido):
    totalsum = contenido.sum()
    return totalsum

def gasto(contenido):
    return contenido.idxmin()

def ahorro(contenido):
    return contenido.idxmax()

def media(contenido):
    return contenido.mean()

def sumgastos(contenido):
    return contenido[contenido < 0].sum()

def sumahorros(contenido):
    return contenido[contenido > 0].sum()

def grafico(contenido):
    fig = px.line(x=contenido.index, y=contenido)
    fig.show()

def main():
    df= lectura_fichero()
    df = comp_cont(df)
    print('\nEl mes que más gasto ha habido ha sido el mes de '+gasto(suma(df)))
    print('\nEl mes que más se ha ahorrado ha sido '+ahorro(suma(df)))
    print('\nLa media de gasto durante el año ha sido de '+str(media(suma(df))))
    print('\nLos gastos totales a lo largo del año han sido de '+str(sumgastos(suma(df))))
    print('\nLos ingresos totales a lo largo del año han sido de '+str(sumahorros(suma(df))))
    grafico(suma(df))


if __name__ == "__main__":
    main()
