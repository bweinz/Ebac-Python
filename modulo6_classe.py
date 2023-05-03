#Modulo 06 de Python - Classes, Programação Orientada a Objetos

'''
uma classe pode ser descrita como um molde, uma receira para criação de objetos
A partir de uma classe, pode-se criar diversos objetos.
Cada classe possui seus atributos e metodos


Sintaxe:
class NomeClasse(object):

  def __init__(self, params):
    self.atributo1 = ...
    self.atributo2 = ...

  def metodo1(self, params):
    ...

  def metodo2(self, params):
    ...
'''

#Dentro de cada classe colocamos as caracteristicas = atributos e os comportamentos = metodos.
class pessoa(object):
    def __init__(self, nome, idade, documento):             # init é uma inicialização do objeto, self descreve se será "vinculado" a classe
        self.nome = nome                                    #self.nome = a classe nome do objeto pessoa recebe o nome como paramentro
        self.idade = idade
        self.documento = documento

def falar(self, texto):
    print(texto)

def __str__(self):                                          #é o chamado do metodo string que o print faz, mas no caso é diretamente
    return f'{self.nome}, {self.idade} anos e documento numero {self.documento}'