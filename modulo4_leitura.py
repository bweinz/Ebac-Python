#Modulo 04 de Python - Ebac (Leitura - With)


#Estrutura do With open: With Open - Comando para ler arquivos.
'''with open(file='Caminho do arquivo', mode='Modo de leitura', encoding='Decodificação de caracter') as apelido:'''

'''Metodo de Leitura = Read 
• Quando usamos read não podemos sobrescrever o arquivo.
• Read Lê o arquivo de uma vez, pode ser um problema com arquivos grandes.'''

#Com open abre arquivo modulos sem / por estar na mesma pasta, modo de leitura, com codificação UTF8, seu nome temporario sera arquivo
with open(file='modulo04_banco.csv', mode='r', encoding='utf8') as arquivo:
    conteudo = arquivo.read()                                                   #Conteudo recebe a leitura do conteudo de arquivo
print(conteudo)

''' COnteudo = 
age,job,marital,education,default,balance,housing,loan
30,unemployed,married,primary,no,1787,no,no
33,services,married,secondary,no,4789,yes,yes
35,management,single,tertiary,no,1350,yes,no
30,management,married,tertiary,no,1476,yes,yes
59,blue-collar,married,secondary,no,0,yes,no
35,management,single,tertiary,no,747,no,no
36,self-employed,married,tertiary,no,307,yes,no
39,technician,married,secondary,no,147,yes,no
41,entrepreneur,married,tertiary,no,221,yes,no
43,services,married,primary,no,-88,yes,yes
'''



'''Metodo de leitura readline()
• Lê o arquivo linha por linha, bom para arquivos grandes, principalmente se quisermos apenas algumas informações.
'''
conteudo = []
with open(file='modulo04_banco.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline() #Vai ser a primeira linha do arquivo CSV (lembrando que é age,job,marital,education,default,balance,housing,loan)
    while linha:
        conteudo.append(linha)
        linha = arquivo.readline() # lê uma nova linha, se a linha não existir, salva o valor None

print(conteudo)      #['age,job,marital,education,default,balance,housing,loan\n', '30,unemployed,married,primary,no,1787,no,no\n', '33,services,married,secondary,no,4789,yes,yes\n', '35,management,single,tertiary,no,1350,yes,no\n', '30,management,married,tertiary,no,1476,yes,yes\n', '59,blue-collar,married,secondary,no,0,yes,no\n', '35,management,single,tertiary,no,747,no,no\n', '36,self-employed,married,tertiary,no,307,yes,no\n', '39,technician,married,secondary,no,147,yes,no\n', '41,entrepreneur,married,tertiary,no,221,yes,no\n', '43,services,married,primary,no,-88,yes,yes\n']
                     #vai ter o mesmo valor que o exemplo do read de cima, porem em uma lista, cada posição da lista terá uma linha do arquivo.


'''Pegando apenas uma coluna do arquivo'''
idades = []

with open(file='modulo04_banco.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # Lê o Cabeçalho (1 linha)
    linha = arquivo.readline()  # Lê as primeiras informaçãoes (2 Linha)
    while linha:
        linha_separa = linha.split(sep=',')    #Pegou a linha, vê onde ter virgulas e quebra cada palavra em uma posição, como idade é a primeira sua posição é index 0
        idade = linha_separada[0]              #variavel idade recebe o valor que estiver na linha posição 0
        idade = int(idade)                     #Esse valor recebido é convertido para o tipo int
        idades.append(idade)                   #Adiciona esse valor na lista idades
        linha = arquivo.readline()             #Lê uma nova linha, se a linha não existir, salva o valor None

