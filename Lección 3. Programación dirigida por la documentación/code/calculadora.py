import sys
class calculadora:
    """Calculadora desarrollada en la asignatura de Progamación Avanzada en Python.

    Atributos
    ----------
    arg1:
        primer argumento
    arg2:
        segundo argumento
    
    funciones
    sumar:
        Suma arg1 y arg2
    restar:
        Resta arg1 y arg2
    multiplicar:
        Multiplica los arg1 y arg2
    dividir:
        Divide los arg1 y arg2
    elevar:
        Eleva el arg1 a la potencia indicada con el arg2

    Ejemplos de uso
    ---------------
    >>> import calculadora
    >>> calc = calculadora(2,2)
    >>> calc.sumar()
    >>> calc.restar()
    >>> calc.multiplicar()
    >>> calc.dividir()  
    >>> calc.elevar()
    """
    def __init__(self, arg1, arg2):
        try:
            self.arg1 = float(arg1)
            self.arg2 = float(arg2)
            val1 = int(arg1)
            val2 = int(arg2)
        except(ValueError):
            print("Uno de los argumentos no es un número. Vuelva a intentarlo")
            sys.exit()

    def sumar(self):
        sumar = self.arg1 + self.arg2
        print( str(self.arg1), "+", str(self.arg2), "=", str(sumar))
    def restar(self):
        restar = self.arg1 - self.arg2
        print( str(self.arg1), "-", str(self.arg2), "=", str(restar))
    def multiplicar(self):
        multiplicar = self.arg1 * self.arg2
        print( str(self.arg1), "*", str(self.arg2), "=", str(multiplicar))
    def dividir(self):
        try:
            dividir = self.arg1 / self.arg2
            print( str(self.arg1), "*", str(self.arg2), "=", str(dividir))
        except(ZeroDivisionError):
            print("Error, el dividisor es 0")
    def elevar(self):
        elevar = self.arg1 ** self.arg2
        print( str(self.arg1), "^", str(self.arg2), "=", str(elevar))


