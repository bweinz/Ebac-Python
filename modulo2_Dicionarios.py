#Modulo 02 de Python enfase em Data Science - Ebac (Dicionarios)

''' Dicionarios são estruturas de armazenamento parecidos com listas porém armazenam sequências no formato chave-valor
• Type dict {}
• Não permitem chaves duplicadas
• Trabalham com Chave - Valor (key - Values)
'''


'''Armazenamento com chave e valor:'''

brasil = {'capital': 'Brasília', 'idioma': 'Português', 'populacao': 210}



'''Não permite duplicidade de chaves:'''
carro = {
    'marca': 'Volkswagen',
    'modelo': 'Polo',
    'ano': 2021,                        #Ele descarta a primeira chave duplicada (ano)
    'ano': 2004
}
print(carro)                            #{'marca': 'Volkswagen', 'modelo': 'Polo', 'ano': 2004}



'''Dicionarios Compostos:'''
cadastro = {
    'andre': {
        'nome': 'Andre Perez',
        'ano_nascimento': 1992,
        'pais': {
            'pai': {
              'nome': '<nome-do-pai> Perez',
              'ano_nascimento': 1971
            },
            'mae': {
              'nome': '<nome-da-mae> Perez',
              'ano_nascimento': 1973
            },
        }
    }
}
print(cadastro['andre']['pais']['mae']['ano_nascimento'])               #1973


'''Operações:'''
credito = {'cpf1': 750, 'cpf2': 980}
#Colocoar o valor dentro de uma variavel, acessando pela sua chave
valorcpf1 = credito['cpf1']
valorcpf2 = credito['cpf2']
print(valorcpf1, valorcpf2)                   #750 980

#Atualizando o valor com atribuição.
credito['cpf1'] = 800
print(credito)                                #{'cpf1': 800, 'cpf2': 980}

'''Métodos'''
#Pode-se criar um dicionario utilizando var = dict():
dicionario = dict (
    nome='Bruno',
    idade=30,
    altura=1.80,
    peso=100,
    cidade='Piracicaba'
)
print(dicionario)                   #{'nome': 'Bruno', 'idade': 30, 'altura': 1.8, 'peso': 100, 'cidade': 'Piracicaba'}

#Além de atrubuição, pode adicionar um valor utilizando .update
dicionario.update({'peso': 80})     #Modificando com Update.
print(dicionario)                   #{'nome': 'Bruno', 'idade': 30, 'altura': 1.8, 'peso': 80, 'cidade': 'Piracicaba'}
dicionario['peso'] = 90             #Modificando com atribuição
print(dicionario)                   #{'nome': 'Bruno', 'idade': 30, 'altura': 1.8, 'peso': 90, 'cidade': 'Piracicaba'}

#Podemos remover utilizando o metodo .pop(key)
dicionario.pop('peso')              #Excluindo a chave e o valor de Peso
print(dicionario)                   #{'nome': 'Bruno', 'idade': 30, 'altura': 1.8, 'cidade': 'Piracicaba'}

#Podemos um novo objeto dentro do dicionario apenas dizendo o nome e o valor:
dicionario['novo'] = 'Nova informação'
print(dicionario)                   #{'nome': 'Bruno', 'idade': 30, 'altura': 1.8, 'cidade': 'Piracicaba', 'novo': 'Nova informação'}


'''Conversão'''
#Podemos converter chaves e valores de um dicionario em listas.

chaves = list(dicionario.keys())    #Pega todas as chaves de dicionario
print(chaves)                       #['nome', 'idade', 'altura', 'cidade', 'novo']

valores = list(dicionario.values()) #Pega todos os valores de dicionario
print(valores)                      #['Bruno', 30, 1.8, 'Piracicaba', 'Nova informação']


'''Exercicio motivação, colocar 2 dicionarios em uma lista.'''

wifi_disponiveis = []
rede = {'nome': 'rede1', 'senha': 'cnx_cnx'}
wifi_disponiveis.append(rede)
rede = {'nome': 'uai-fi', 'senha': 'r3d3'}
wifi_disponiveis.append(rede)
print(wifi_disponiveis)                     # [{'nome': 'rede1', 'senha': 'cnx_cnx'}, {'nome': 'uai-fi', 'senha': 'r3d3'}]



'''Obs:

1º - Usaremos a lista como se fosse um array de javascript, funcionando para armazenamento de varias informações de diferentes tipos de dados

2º - Conjuntos (set) usaremos quase que exclusivamente para arrumar problemas de duplicidade em listas

3º - Dict, seu diferencial é que o index em vez de ser numerico é por meio de chaves que se comportam como se fosse por exemplo a criação de um objeto em Javascript, permitindo que crie niveis de parentesco das informações
'''
