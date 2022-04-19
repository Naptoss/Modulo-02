
print()
print('{0:_^40}'.format("   Calculadora    "))
print("Ola, Bem vindo a calculadora do tobas, você gostaria de usar-la ?")
s = input("s[im] ou n[ão]: ")
print('{0:_^25}'.format('_'))
if s.lower() == "n": exit() 




print('{0:_^25}'.format('_'))
num_1 = input("Digite um numero: ")
    
operador = input("Digite um operador: ")
    
num_2 = input("Digite outro numero: ")
print('{0:_^25}'.format('_'))
    

if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um numero valido ")

num_1 = int(num_1)
num_2 = int(num_2)

    
if operador == "+":
        print(num_1 + num_2)
elif operador == "x":
        print(num_1 * num_2) 
elif operador == "-":
        print(num_1 - num_2)
elif operador == "%":
        print(num_1 / num_2)
    
else:
    print("Operador invalido, insira um correto")
    

print("Gostaria de continuar utilizando a calculadora: ")
p = input("s[im] ou n[ão]: ")
if p.lower() == "n": exit = False

    
        
        


    
    

    