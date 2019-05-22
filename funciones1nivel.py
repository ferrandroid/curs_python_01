''' Exemple de com una funció es pot
    assimilar a un paràmetre o variable '''

# FUNCIONS DE PRIMER NIVELL
# = que admeten funcions com paràmetres d'entrada

# Aquesta funció simplement retorna el número
def normal(x):
    return x

# Aquesta funció simplement retorna el quadrat
def cuadrado(x):
    return x*x

# El segon paràmetre recupera la funció
def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
        
    return resultado

print (sumaTodos(3, normal))
print (sumaTodos(3, cuadrado))