#import pdb 
#pdb.set_trace()
listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
maximos = [print(max(lista)) for lista in listas]

lista_2 = [3, 4, 8, 5, 5, 22, 13,23]
primos = list(filter(lambda x: all(x%i!=0 for i in range(2, x//2)), lista_2))
print(primos)