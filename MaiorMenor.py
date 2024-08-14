#Calcular o maior e o menor elemento de uma lista
def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
        elif elemento < menor:
            menor = elemento
        return maior, menor
    #Entrada de dados onde o 'cliente' irá entrar com os dados
    lista=list()
    i=1
    while i<=10:
        elem = int(input('Digite um elemento da lista: '))
        lista.append(elem)
        i+=1
    print(lista)

#Apresentação dos Resultados
maior, menor = maior_menor(list)
print('Maior: ', maior)
print('Menor: ', menor)