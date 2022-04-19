"""


t1 = (1,2,3,4,5) <---- Tupla nao consegue editar uma lista
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)


entretanto, da pra converter ela como esta na linha 5 a 7.

"""