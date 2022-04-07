import pandas as pd

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
    return contenido.min()

def ahorro(contenido):
    return contenido.max()

def media(contenido):
    return contenido.mean()

def main():
    df= lectura_fichero()
    print(df)
    columnas(df)
    df = comp_cont(df)
    print(gasto(suma(df)))
    print(ahorro(suma(df)))
    print(media(suma(df)))
    print(suma(suma(df)))



if __name__ == "__main__":
    main()
