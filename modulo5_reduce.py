#Modulo 05 de Python - Reduce

'''
Vai aplicar uma função em elementos da coleção, ela vai aplicar a função em 2 elementos por vez, até que sobre apenas um elemento

variavel = reduce(função, coleção)

a função obrigatoriamente vai retornar um valor.
'''

numeros = [1,2,3]
from functools import reduce                    #Biblioteca importada
soma = reduce(lambda x,y: x + y, numeros)
print(soma)                                     #6

'''
Ele vai pegar os valores da lista = 1,2,3

A função lambda pede dois parametros x e y
 x = 1 e y = 2    x + y = 3
A proxima iteração, x vai valer o resultado da ultima operação: x = 3 e o proximo valor da lista sera o Y:
 x = 3 e y = 3    x + y = 6
por isso sempre sera de 2 em 2 até restar apenas 1
Lembrando que a função poderia ser pedindo qualquer outro tipo de informação.
'''
#Fazendo a comparação de dois valores com uma função propria
def maior_entre(primeiro, segundo):
  return primeiro if primeiro >= segundo else segundo           #Retorne primeiro Se primeiro for maior ou igual segundo, senão retorne segundo
primeiro = 12
segundo = 11
print(maior_entre(primeiro=primeiro, segundo=segundo))

import random
numeros = [random.randint(1, 100) for _ in range(0, 100)]       #Para um alcance de 0 a 99, adicione os valores aleatorios gerados de 0 a 100 e coloque na lista [numeros]
print(numeros)

#Usando a def criada anteriormente
maior_numero = reduce(maior_entre, numeros)                     #Vai testar de 2 em 2 valores quel é o maior valor e retornar
print(maior_numero)

#Usando a função lambda direta:
maior_numero = reduce(lambda primeiro, segundo: primeiro if primeiro >= segundo else segundo, numeros)
print(maior_numero)


'''
Utilizando todos os metodos juntos:
'''

import random
numeros = [random.randint(1, 100) for _ in range(0, 100)]                                                                           #define a lista com valores aleatorios de 1 a 99

numeros_ao_quadrado = map(lambda numero: numero ** 2, numeros)                                                                      #Vai elevar todos os valores ao quadrado

numeros_impares = filter(lambda numero: numero % 2 != 0, numeros_ao_quadrado)                                                       #Vai filtrar quais numeros são Impares ou seja Diferentes de 0

soma_numeros = reduce(lambda x, y: x + y, numeros_impares)                                                                          #Vai somar os valores impares
print(soma_numeros)

soma_numeros = reduce(lambda x, y: x + y, filter(lambda numero: numero % 2 != 0, map(lambda numero: numero ** 2, numeros)))
print(soma_numeros)