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
n=int(input("Insira um numero: "))  #valor do triangulo
iterador=0              #variavel para iterar pelo loop
tam_while=n*2           #tamanho do while loop
char='*'
char_multi=0            #multiplicador do char
while(iterador<tam_while):
    if(iterador<tam_while/2):
        char_multi+=1
        print(f"{char*char_multi}")
        iterador+=1
    elif(iterador>=tam_while/2):
        char_multi-=1
        print(f"{char*char_multi}")
        iterador+=1