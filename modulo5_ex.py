'''
%%writefile credito.csv
id_vendedor,valor_emprestimos,quantidade_emprestimos,data
104271,448.0,1,20161208
21476,826.7,3,20161208
87440,313.6,3,20161208
15980,-8008.0,6,20161208
215906,2212.0,5,20161208
33696,2771.3,2,20161208
33893,2240.0,3,20161208
214946,-4151.0,18,20161208
123974,2021.95,2,20161208
225870,4039.0,2,20161208
'''
emprestimos = []
with open(file='modulo5_ex_credito.csv', mode='r', encoding='utf8') as fp:
  fp.readline() # cabeçalho
  linha = fp.readline()
  while linha:
    linha_emprestimo = {}
    linha_elementos = linha.strip().split(sep=',')
    linha_emprestimo['id_vendedor'] = linha_elementos[0]
    linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
    linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
    linha_emprestimo['data'] = linha_elementos[3]
    emprestimos.append(linha_emprestimo)
    linha = fp.readline()

for emprestimo in emprestimos:
    #print(emprestimo)
    '''
    {'id_vendedor': '104271', 'valor_emprestimos': '448.0', 'quantidade_emprestimos': '1', 'data': '20161208'}
{'id_vendedor': '21476', 'valor_emprestimos': '826.7', 'quantidade_emprestimos': '3', 'data': '20161208'}
{'id_vendedor': '87440', 'valor_emprestimos': '313.6', 'quantidade_emprestimos': '3', 'data': '20161208'}
{'id_vendedor': '15980', 'valor_emprestimos': '-8008.0', 'quantidade_emprestimos': '6', 'data': '20161208'}
{'id_vendedor': '215906', 'valor_emprestimos': '2212.0', 'quantidade_emprestimos': '5', 'data': '20161208'}
{'id_vendedor': '33696', 'valor_emprestimos': '2771.3', 'quantidade_emprestimos': '2', 'data': '20161208'}
{'id_vendedor': '33893', 'valor_emprestimos': '2240.0', 'quantidade_emprestimos': '3', 'data': '20161208'}
{'id_vendedor': '214946', 'valor_emprestimos': '-4151.0', 'quantidade_emprestimos': '18', 'data': '20161208'}
{'id_vendedor': '123974', 'valor_emprestimos': '2021.95', 'quantidade_emprestimos': '2', 'data': '20161208'}
{'id_vendedor': '225870', 'valor_emprestimos': '4039.0', 'quantidade_emprestimos': '2', 'data': '20161208'}
    '''

#Converter os valores para float
valor_emprestimos_lista = list(map(lambda emprestimo: float(emprestimo['valor_emprestimos']), emprestimos))
print(valor_emprestimos_lista)

#Filtrar os valores maiores do que zero
valor_emprestimos_lista_filtrada = list(filter(lambda valor: valor > 0, valor_emprestimos_lista))
print(valor_emprestimos_lista_filtrada)

#Reduce para extrair a soma
from functools import reduce
soma_valor_emprestimos = reduce(lambda x, y: x + y, valor_emprestimos_lista_filtrada)
print(soma_valor_emprestimos)

#Extrair a média aritimética
media_valor_emprestimos = reduce(lambda x, y: x + y, valor_emprestimos_lista_filtrada ) / len(valor_emprestimos_lista_filtrada)
print(media_valor_emprestimos)

#Extrair o desvio padrão
desvio_padrao_valor_emprestimos = (reduce(lambda x, y: x + y, map(lambda x: (x - media_valor_emprestimos)**2, valor_emprestimos_lista_filtrada)) / (len(valor_emprestimos_lista_filtrada) - 1)) ** 0.5
print(desvio_padrao_valor_emprestimos) # 1271.997271149785