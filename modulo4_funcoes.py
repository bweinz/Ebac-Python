#Modulo 04 de Python - Ebac Funções:
''' Definição: um bloco de código que só é executado quando chamado, muito utilizado para repetir códigos.'''


'''Estrutura:
def <nome>(<param 1>, <param 2>, ...):
  bloco de código
  return <valor de retorno>
var = <nome da funcao>(<param 1>, <param 2>, ...)
'''

#Exemplo:
def imprime(mensagem):
    print(mensagem)

texto = 'Banana'
imprime(mensagem='Exemplo') #podemos especificar o que queremos, dizendo que mensagem vale = exemplo
imprime(texto)              #podemos pedir para rodar a função tendo como o parametro mensagem o conteudo de texto


'''Return
Toda função retorna pelo menos um valor, se não específicado, retorna o valor nulo'''

#Sem especificações de parametro:
def maiusculo(texto):
  text_maiusculo = texto.upper()
  return text_maiusculo
nome = 'André Perez'
print(nome)
nome_maiusculo = maiusculo(nome)
print(nome_maiusculo)


#Com especificação de Parametro:
def maiusculo(texto: str) -> str:          #Declaramos que a entrava vai ser de um tipo string texto: str e o valor retornado vai ser string também -> str
  text_maiusculo = texto.upper()
  return text_maiusculo
nome = 'André Perez'
print(nome)
nome_maiusculo = maiusculo(texto=nome)     #Declaramos que o valor do texto é igual a variavel nome
print(nome_maiusculo)


'''Funções com parâmetros variados:'''
#Exemplo sem Especificação
def escreverArquivo(nome, cabecalho, conteudos):                            #crie a função escreverArquivo que recebera 3 parametros
    try:                                                                    #tente
        with open(file=nome, mode='w', encoding='utf8') as fp:              #Escreva(w) um arquivo com nome provisorio de fp:
            linha = cabecalho + '\n'                                        #Primeira linha = cabeçalho e pula de linha
            fp.write(linha)                                                 #Escreva a linha atual
            for conteudo in conteudos:                                      #Para cada conteudo dentro da lista conteudos:
                linha = str(conteudo) + '\n'                                #transforme o conteudo em string
                fp.write(linha)                                             #Escreva o conteudo
    except Exception as exc:                                                #Caso tenha algum erro, nomeie como erro
        print(exc)                                                          #escreva o nome do erro
        return False                                                        #se houver um erro retorne que foi falso
    return True                                                             #Se não houver erro, retorne True e terá criado o arquivo

nome = 'modulo04_idades-funcao.csv'                                         #parametro nome
cabecalho = 'idade'                                                         #parametro cabecalho
conteudos = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43]                        #parametro lista conteudos

escreveu_com_sucesso = escreverArquivo(nome, cabecalho, conteudos)          #Variavel escreveu_com_sucesso recebe a função escreverArquivo com os parametros passados
print(escreveu_com_sucesso)
#Printa se conseguiu criar a tabela sem erro (TRUE) ou se teve algum erro (False)


#Exemplo, mesmo código utilizando especificações:
def escreve_arquivo_csv(nome: str, cabecalho: str, conteudos: list) -> bool:        #O valor de nome vai ser uma string, de cabeçalho uma string, conteudo uma lista) e retornara uma booleano -> bool
    try:
        with open(file=nome, mode='w', encoding='utf8') as fp:
            linha = cabecalho + '\n'
            fp.write(linha)
            for conteudo in conteudos:
                linha = str(conteudo) + '\n'
                fp.write(linha)
    except Exception as exc:
        print(exc)
        return False
    return True

nome = 'idades-funcao-erro.csv'
cabecalho = 'idade'
conteudos = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43]
#conteudos = 10

escreveu_com_sucesso = escreve_arquivo_csv(nome=nome, cabecalho=cabecalho, conteudos=conteudos)
print(escreveu_com_sucesso)