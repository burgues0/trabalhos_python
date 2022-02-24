#Algoritmos Computacionais e Estruturas de Dados 
#2a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 13/09/2021
#Turma 2BINFO
#Alunos:
#Victor Kauã Martins Nunes
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Pinheiro Palmeira
n=int(input("Insira um valor: "))
n1=1                                #primeira parte do programa:
n2=1                                #descobrir os 2 maiores
iterador=0                          #dos 'n' primeiros valores
while(iterador<=n):                #da serie de fibonacci
    n3=n1+n2
    n1=n2
    n2=n3
    iterador+=1
maior=n2                         #maior valor
pre_maior=n1                 #segundo maior valor
iterador=0
while(iterador<n+1):                #segunda parte do programa:
    j=maior                         #descobrir o fatorial
    fatorial=1                      #dos valores encontrados
    while(j>1):                     #e ir printando os *
        fatorial*=j                 #de trás pra frente
        j-=1
    print('*' * fatorial)
    aux=maior
    maior=pre_maior
    pre_maior=aux-pre_maior
    iterador+=1