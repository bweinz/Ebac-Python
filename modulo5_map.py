#Modulo 05 de Python - MAP
'''
variavel = map(função, coleção)

coleção: list, Dict

Para cada elemento da coleção o map vai aplicar a função

'''


numeros = [1,2,3]
numeroAoCubo = map(lambda num: num ** 3, numeros)               #Map para varrer a coleção com a função, (lambda é uma função que tem como paremetro num que retorna : num elevado a 3, do conjunto numeros)
print(list(numeroAoCubo))                                       #Precisamos retornar o valor em uma lista, se não colocar list não aparece o resultado.  1,8,27

#Cortando o provedor do Email:
emails = ['brunoweinz@hotmail.com', 'brunoweinz@outlook.com']
extrairProvedor = lambda email: email.split('@') [-1]


#Fazendo com For
provedores = []
for email in emails:
    provedor = extrairProvedor(email)
    provedores.append(provedor)
print(provedores)                                                   #['hotmail.com', 'outlook.com']

#Fazendo com Map
provedores = list(map(extrairProvedor, emails))
print(provedores)                                                   #['hotmail.com', 'outlook.com']

#Map diretamente com Lambda
provedores = map(lambda email: email.split('@')[-1], emails)
print(list(provedores))                                             #['hotmail.com', 'outlook.com']


#Exemplo com mais de um parâmetro:
anos = [10, 10, 10]
taxas_juros = [0.05, 0.10, 0.15]
valores_iniciais = [1000, 1000, 1000]

def retorno(valor_inicial: float, taxa_juros: float, anos: int) -> float:
  valor_final = valor_inicial
  for ano in range(1,anos+1):
    valor_final = valor_final * (1+taxa_juros)
  return round(valor_final, 2)

cenarios = list(map(retorno, valores_iniciais, taxas_juros, anos))
print(cenarios)                                                       #[1628.89, 2593.74, 4045.56]

''' 
No caso de mais de 1 parametro ele vai testar as 3 combinações ao mesmo tempo: 
(10, 0.05 e 1000)  = 1628,89
(10, 0.10 e 1000)  = 2593,74
(10, 0.15 e 1000)  = 4045,56
'''