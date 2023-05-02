#Modulo 05 de Python - Filter

'''
Funciona muito parecido com o Map, porém ele vai retornar valores booleanos, iremos trabalhar em cima do retorno True or False.
Sua estrutura também é como a do Map, vai passar uma função que vai correr em todos as posições da coleção.

varial = filter(função, coleção)
'''


numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_par = filter(lambda num: num % 2 == 0, numeros)             #Ele vai testar a função lambda, se caso o numero divisão por 2, tiver resto 0 (par- TRUE), ele vai adicionar em numeros_par.
print(list(numeros_par))                                            #[2, 4, 6, 8, 10]



#Declaração da Lista de emails
emails = ['brunoweinz@hotmail.com', 'brunoweinz@outlook.com', 'brunoweinz@gmail.com']


#Colocando a função lambda em uma variavel (desnecessario)
provedor_da_google = lambda email: 'gmail' in email

#resolvendo com For:
emails_google = []
for email in emails:
    if provedor_da_google(email) == True:
        emails_google.append(email)
print(emails_google)                                                #['brunoweinz@gmail.com']


#resolvendo com Filter e função declarada anteriormente:
emails_google = filter(provedor_da_google, emails)
print(list(emails_google))                                          #['brunoweinz@gmail.com']

#resolvendo com Filter diretamente:
emails_google = filter(lambda email: 'gmail' in email, emails)
print(list(emails_google))                                          #['brunoweinz@gmail.com']

