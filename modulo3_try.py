#Modulo 03 de Python - Ebac (Try Except e Finally)
#Try tem uma estrutura parecida com if

'''
try:
    tente rodar esse codigo
except
    se tiver esse erro(especifico) ou qualquer outro error faça tal coisa.
finally:
    finalmente depois de tudo faça isso indepente do resultado do try e do except
'''


'''Exemplo de try quando sabemos o posivel erro:'''
preco = 132.85
pessoas = 0
try:                                        #tente
    divisao = preco / pessoas               #Fazer preço dividido por pessoas
except ZeroDivisionError:                   #Caso tenha um erro de Divisão por zero
    print('Numero de pessoas invalido')     #Printe Numero de pessoas invalido



'''NÃO sabemos o possivel erro:'''
anos = [2019, 2020, 2021]
try:
    ano_atual = anos[3]
except Exception:                           #caso tenha um erro = erro
    print('Aconteceu uma exceção(error)')



'''Não sabemos o possivel erro mais queremos pega-lo'''
n = 30
pessoas = 0

try:
    divisao = n / pessoas
except Exception as nomeEscolhidoParaoErro:
    print(f'O nome do error é {str(nomeEscolhidoParaoErro)}')           #O nome do error é division by zero
    print(f'O tipo do erro é {str(type(nomeEscolhidoParaoErro))}')      #O tipo do erro é <class 'ZeroDivisionError'>


'''Finally'''
nome = 'Andre Perez'
idade = 19

try:
  apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
  print(apresentacao)
except TypeError:
  idade = str(idade)
finally:
  print('Segunda chance')
  apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
  print(apresentacao)

'''
Try: Tentamos fazer uma operação de concatenação de string e number vai dar um erro:
except: Corrigimos o erro transformando o valor numerico em string
finally: damos uma segunda chance para o programa funcionar

obs: o finally vai executar o que estiver dentro dele independente de ter tratamento de erro no except ou não, ele sempre será executado.

 '''