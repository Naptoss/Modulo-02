def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

lista = [1,2,3,4,5,6]
func(*lista,nome='Antonio',sobrenome='Gabinio')
