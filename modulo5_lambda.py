#Modulo 05 de Python - Lambda

'''
Uma função lambda em Python é uma função anônima, ou seja, uma função que não tem um nome atribuído.
Ela é definida usando a palavra-chave "lambda" seguida de uma lista de argumentos separados por vírgulas
um sinal de dois pontos e uma expressão que é o valor de retorno da função.


• Bloco de código enxuto
• Pode ser salvo em uma variável
• Em geral é utilizada com outros métodos funcionais, Map, filter e reduce
'''

#Exemplo de lambda para extrair o provedor de e-mail
var_extrair_provedor = lambda email: email.split(sep='@')[-1]   #Cria-se um var que vai receber a função lambda email: essa função vai pegar o conteudo da variavel email e aplicar um split de separação a apartir de @
email = "brunoweinz@hotmail.com"                                #brunoweinz@hotmail.com
print(email)
provedor = var_extrair_provedor(email)                          #Nova var provedor vai receber a execução da função var_extrair criada como lambda
print(provedor)                                                 #hotmail.com


#Função Lambda com estruturas condicionais:
numeroPar = lambda numero: True if numero % 2 == 0 else False   #Cria-se uma var que vai receber se o numero % 2 é par (True) senão é (False)
numeros = range(0,10)                                           #vai criar os numeros de 0 a 9

for numero in numeros:                                          #para cada numero criado em numeros faça:
    if numeroPar(numero):                                       #Se a função do numeroPar(com cada numero dos numeros de 0 a 9) ou seja, pega a função para ver se é % 2 == 0, se for Par = TRUE
        print(f'O número {numero} é par')                       #Se for par, printa: O numero 0 é par, O numero 2 é par..... sucessivamente



''' Funções de Alta ordem:
Funções de alta ordem são funções que podem receber outras funções como parâmetros e/ou retornar funções como resultado. 
Em outras palavras, são funções que tratam outras funções como valores.


'''

#Definição:

def retorno(juros):                                             #Cria uma função chamada retorno com o parametro juros
    return lambda investimento: investimento * (1 + juros)      #a função vai retornar uma função lambda chamada investimento, o valor do parametro investimento * (1 + o juros parametro da função principal)

#Instanciação:
retorno5 = retorno(0.05)                                        #Retorno5 é o resultado da chamada da função Retorno
retorno10 = retorno(0.10)

valor5 = retorno5(1000)
print(valor5)

valor10 = retorno10(1000)
print(valor10)

'''
Resumo do Código:
A primeira linha define uma função chamada retorno que recebe um parâmetro chamado juros.
A segunda linha retorna uma função lambda que recebe um parâmetro chamado investimento e retorna o resultado do cálculo de investimento * (1 + juros).
Na primeira linha, a variável retorno5 é criada e recebe o resultado da chamada da função retorno com o argumento 0.05.
Na segunda linha, a variável retorno10 é criada e recebe o resultado da chamada da função retorno com o argumento 0.10.
Na primeira linha, a variável valor5 é criada e recebe o resultado da chamada da função retorno5 com o argumento 1000.
Na segunda linha, o valor de valor5 é impresso na tela usando a função print.
Na terceira linha, a variável valor10 é criada e recebe o resultado da chamada da função retorno10 com o argumento 1000.
Na quarta linha, o valor de valor10 é impresso na tela usando a função print.
Em resumo, o código define uma função que cria funções lambda para calcular o valor de um investimento com juros, e depois chama essas funções para calcular o valor do investimento com juros de 5% e 10% para um investimento de 1000, respectivamente, imprimindo esses valores na tela.
'''

'''Obs: 
Quando você chama a função retorno com um determinado valor de juros, ela retorna uma função que espera receber um valor de investimento como parâmetro.
Então, quando você faz retorno5 = retorno(0.05), você está chamando a função retorno com o valor de juros de 5% e armazenando a função lambda resultante em retorno5. 
Ou seja, retorno5 agora é uma função que espera receber um valor de investimento como parâmetro e calcular o valor do investimento com juros de 5%.
Quando você faz valor5 = retorno5(1000), você está chamando a função lambda armazenada em retorno5 com o valor de investimento de 1000. 
A função lambda realiza o cálculo do valor do investimento com juros de 5% e retorna o resultado, que é armazenado em valor5.
Então, em resumo, retorno5 é uma função que foi criada a partir da função retorno com um valor de juros específico e valor5 é o resultado do cálculo do investimento de 1000 com juros de 5%.
'''


#Exemplo

anos = 10
valorInicial = 1000
valorFinal = valorInicial                      #ValorFinal = 1000

for ano in range(1, anos+1):                   #Para cada ano em um alcance de 1, 11:
    valorFinal = retorno10(valorFinal)         #Valor final vai receber o valor da função retorno10(tendo o valor final como parametro) a cada iteração o valor final vai receber o novo valor e fazer a função de 10% de juros novamente

valorFinal = round(valorFinal,2)               #Valor final vai ser arredondado para 2 casas decimais
print(valorFinal)