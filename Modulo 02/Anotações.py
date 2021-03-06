"""

Tipos de dados 
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/false 10 == 10


+,  - soma
-,  - subtração
*,  - multiplicação
/,  - divisão
//, - divisão inteira
**, - exponenciação
%,  - resto da divisão
()  - 


:s - Texto (strings)
:d - inteiros (int)
:f - pontos flutuantes (float)
:.(NUMERO)f - Quantidades de casa decimais (float) :.2f
:(CARACTERE)(> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - esquerda
< - direita
^ - meio 


variavel = 'alguma str'
print(variavel.lower()) - todo minusculo
print(variavel.uper()) - todo maisculo
print(variavel.title()) - as primeiras letras de cada nome são maiusculas
varial_qtd = len(nome) - pra puxar quantidade de caracteres do nome


if - primeiro a ser puxado
elif - puxado quando o resultado for false
else - quando não houver um elif e o if nao for puxado ele ira dar o resultado(obs: o else nao precisa ser acompanhado de alguma função, apenas com dois ponto(:) )


Continue - pula para o proximo laço 
Break - Termina a ação


Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - retorna um objeto iterável # iteráveis

def - definir um parametro 
return - retornar o valor
*args - definido como um valor x pela comunidade
**kwargs - procura por uma key
Tuplas - a tupla nao consegue editar a lista 
lambda - função anonima, pode ser usada para organizar lista e etc; 

exemplo:
lista = [
    ['P1',5],
    ['P2',54],
    ['P3',12],
    ['P4',10],
    ['P5',19],
    ['P6',11],
    ['P7',23],
]



lista.sort(key=lambda item: item[1], reverse=True)  #<----- aqui ela esta ordenando do maior para o menor, caso queira fazer o inverso basta retirar o reverse
print(lista).

Outro exemplo:

def func(item):   <---- Definiu o item 
    return item[1]        <---- retornou o item 1        

lista.sort(key=func, reverse=True)  <----- Ordenou 
print(lista)

Outro exemplo:

print(sorted(lista, key=lambda i: i[1]))

OBS IMPORTANTE! :


d1 = {'chave1':'valor da chave'}
d1['nova chave'] = 'Valor da nova chave'

print(d1['chave1']) <--- Tudo que estiver entre cochete vai ser o valor que o requerente quer 

add - adiciona
update - atualizar
clear - limpar
discard - discartar 
union - une
intersection & - todos os elementos presentes nos dois sets
difference - elementos apenas no set da esquerda
symmetric_diference ^ - elementos que estao nos dois sets, mas nao em ambos


"""
