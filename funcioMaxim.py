''' Funció que troba el valor màxim dins d'un array
    la notació *l converteix el paràmetre en un array
    de longitud a concretar '''

def valorMax(*l):
    # si l'array no té elements que retorni 0
    if len(l) == 0:
        return 0
    
    # es quedarà en el valor màxim
    maxim = l[0]
    for index in range(1, len(l)):
        if l[index] > maxim :
            maxim = l[index]
            
    return maxim

''' Funció que troba el valor mínim dins d'un array
    la notació *l converteix el paràmetre en un array
    de longitud a concretar '''

def valorMin(*l):
    # si l'array no té elements que retorni 0
    if len(l) == 0:
        return 0
    
    # es quedarà en el valor mínim
    minim = l[0]
    for index in range(1, len(l)):
        if l[index] < minim :
            print(l[index], "és el màxim")
            minim = l[index]
            
    return minim

''' Funció que troba la mitjana aritmètica dins d'un array
    la notació *l converteix el paràmetre en un array
    de longitud a concretar '''
def media(*l):
    # si l'array no té elements que retorni 0
    if len(l) == 0:
        return 0
    
    # es quedarà en el valor mínim
    suma = 0
    for valor in l:
        suma += valor
        
    return suma/len(l)


print( valorMax(1, 200, 4, 45) )
print( valorMin(1, 200, 4, 45) )
print( media(1, 200, 4, 45) )