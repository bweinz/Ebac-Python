#Modulo 02 de Python enfase em Data Science - Ebac (Listas)

''' colchetes []
• Type List
• Definição: Armazenam sequências mutáveis e ordenadas de valores

'''


'''1º pode-se pegar valores de variaveis externas para incorporar a lista:'''
idade = 20
saldo_em_conta = 723.15
usuario_loggedin = True

usuario_web = ['André Perez', idade, 'andre.perez', 'andre123', 'andre.perez@gmail.com', saldo_em_conta, usuario_loggedin]

print(usuario_web)
print(type(usuario_web))



'''2º Concatenação de Listas: Podendo mesclar diversas listas'''
fabricantes_mobile_china = ['xiaomi', 'huawei']
fabricantes_mobile_eua = ['apple', 'motorola']
fabricantes_mobile = fabricantes_mobile_china + fabricantes_mobile_eua

print(fabricantes_mobile_china)             #['xiaomi', 'huawei']
print(fabricantes_mobile_eua)               #['apple', 'motorola']
print(fabricantes_mobile)                   #['xiaomi', 'huawei', 'apple', 'motorola']



'''3º Slicing: Pode ser usado o fatiamento diretamente nas posições (index) da lista:'''
fabricantes_mobile_china = fabricantes_mobile[0:2]
fabricantes_mobile_eua = fabricantes_mobile[2:len(fabricantes_mobile)]

print('china: ' + str(fabricantes_mobile_china))        #china: ['xiaomi', 'huawei']
print('eua: ' + str(fabricantes_mobile_eua))            #eua: ['apple', 'motorola']

#Obs: transforma a lista em uma String para poder concatenar com 'china', não é permitido concatenar str com list, apenas list com list ou str com str



'''4º Mutabilidade: Trocar valores de dentro da lista:'''
fabricantes_mobile[2] = 'nokia'
print(fabricantes_mobile)



'''5º METODOS DE LISTAS:'''
juros = [0.05, 0.07, 0.02, 0.04, 0.08]

# inserir um elemento sem substituir: list.insert(index, value)
juros.insert(0, 0.10)
print(juros)            #[0.1, 0.05, 0.07, 0.02, 0.04, 0.08]

# inserir um elemento no fim da lista: list.append(val)
juros.append(0.09)
print(juros)            #[0.1, 0.05, 0.07, 0.02, 0.04, 0.08, 0.09]

# remover um elemento pelo valor: list.remove(value)
juros.remove(0.1)
print(juros)            #[0.05, 0.07, 0.02, 0.04, 0.08, 0.09]   (Removeu o valor 0.1)

# remover um elemento pelo índice: list.pop(index)
terceiro_juros = juros.pop(2)
print(terceiro_juros)   #0.02 (valor que foi excluido)



'''6º Conversão de variáveis em listas, como strings:'''
email = 'andre.perez@gmail.com'
caracteres_email = list(email)          #Transforma cada caractere de email em uma posição na lista

print(email)
print(caracteres_email)                 #['a', 'n', 'd', 'r', 'e', '.', 'p', 'e', 'r', 'e', 'z', '@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o', 'm']


#7º Motivação:
dia_11_saldo_inicial = 1000

dia_11_transacoes = []

dia_11_transacoes.append(243)
dia_11_transacoes.append(-798.58)
dia_11_transacoes.append(427.12)
dia_11_transacoes.append(-10.91)

print(dia_11_transacoes)
dia_11_saldo_final = dia_11_saldo_inicial + dia_11_transacoes[0] + dia_11_transacoes[1] + dia_11_transacoes[2] + dia_11_transacoes[3]
print(dia_11_saldo_final)

#Resultado: 860.63