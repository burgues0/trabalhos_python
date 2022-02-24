#Algoritmos Computacionais e Estruturas de Dados 
#1a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 23/08/2021
#Turma 2BINFO
#Alunos:
#Victor Kauã Martins Nunes
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Pinheiro Palmeira
dd = int(input())
mm = int(input())
aa = int(input())

if(((mm ==  4 or mm == 6 or mm == 9 or mm == 11) and dd > 30) or (mm == 2 and dd > 28) or (dd > 31) or (dd <= 0)): #Verificar se é uma data válida ou não
    print("Data inválida")
else:
    if(((mm ==  4 or mm == 6 or mm == 9 or mm == 11) and dd == 30)): #Todos os meses que terminam em 30
        print(f"01, {mm + 1}, {aa}")
    elif((mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10) and dd == 31): #Todos os meses que terminam em 31
        print(f"01, {mm + 1}, {aa}")
    elif(mm == 2 and dd == 28): #Fevereiro acaba no dia 28 caso nao seja um ano bissexto
        print(f"01, {mm + 1}, {aa}")
    elif(mm == 2 and dd == 28 and ((aa % 4 == 0 and aa % 100 != 0) or aa % 400 == 0)): # um ano bissexto é um ano que é divisivel por 4, mas não pode ser divisivel por 100 (a menos que seja divisivel por 400)
        print(f"{dd + 1}, {mm}, {aa}")
    elif(mm == 12 and dd == 31):    #ano novo
        print(f"01, 01, {aa + 1}")
    else: #Caso nao seja nenhum destes casos, apenas adicione 1 dia
        print(f"{dd + 1}, {mm}, {aa}")
