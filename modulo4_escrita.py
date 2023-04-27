#Modulo 04 de Python - Ebac (Escrita - With)

'''
r mais seguro
w = cria ou reescreve destroi o anterior
a = acrescenta em cima do arquivo, na ultima linha.
'''


#Apenas Base para aula de Escrita
idades = []
with open(file='modulo04_banco.csv', mode='r', encoding='utf8') as arquivo:
  linha = arquivo.readline() # lê o cabeçalho
  linha = arquivo.readline() # lê a primeira linha
  while linha:
    linha_separada = linha.split(sep=',') # quebra a string nas virgulas e salva os resultados em uma lista
    idade = linha_separada[0] # seleciona o primeiro elemento da lista
    idade = int(idade) # converte o valor de string para integer (inteiro)
    idades.append(idade) # salva o valor na lista de idades
    linha = arquivo.readline() # lê uma nova linha, se a linha não existir, salva o valor None
print(idades)

'''
r: Abrir o arquivo para leitura (padrão);
w: Abrir o arquivo para escrita (sobreescreve o arquivo original).
a: Abrir o arquivo para acrescentar (não sobreescreve o arquivo original)
'''

'''Modo de escrita (w)'''

with open(file='modulo04_idades.csv', mode='w', encoding='utf8') as fp:
    linha = 'idade' + '\n'              #Cabeçalho, 1º Linha recebe o titulo Idade e pula uma linha
    fp.write(linha)                     #No arquivo fp. escreva Linha
    for idade in idades:                #Para cada idade no exemplo de leitura que tiramos a coluna inteira e criamos a lista idades.
        linha = str(idade) + '\n'       #o valor numero de idade é transformado para string e pulamos linha novamente
        fp.write(linha)                 #Escreva a linha.

#Este codigo vai pegar as informações da coluna e criar um arquivo csv novo com essas informações.


'''Modo de escrita (a)
Este modo é igual o W, porem ele é de acrescimo, ele não sobrescreve, ele adiciona as informações no final do arquivo'''

with open(file='modulo04_idades.csv', mode='a', encoding='utf8') as fp:
    for idade in idades:
        linha = str(idade + 100) + '\n'
        fp.write(linha)

#este codigo ira acrescer abaixo dos valores do codigo de cima, os mesmos valores + 100 (visualize no documento modulo04_idades