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
balas=5
rodando=True        #bool para checar se outra checagem de tentativa do caçador deva ocorrer
valor1 = int(input('O Marciano está em qual das 1 a 100 arvores? Digite um valor nesse espaço: \n'))
if(valor1<1 or valor1>100):         #condicional de funcionamento do programa
    print('O valor da arvore não está entre 1 e 100.')
else:
    
    if(rodando==True):     
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n')) #primeiro tiro
        
        if(valor2<1 or valor2>100): #condicional de funcionamento do programa(se repete ao longo das tentativas)
            print("\nValor inválido.")
        else:
            if(valor1==valor2):     #caso o caçador acerte
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO!') #caso acerte troca a condição pra False e para as checagens
                rodando=False
            else:
                if(valor1>valor2):  #caso ele erre
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('Tente Novamente até acabar suas balas.')
                    print('O marciano está mais a direita.')
                elif(valor1<valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('Tente Novamente até acabar suas balas.')
                    print('O marciano está mais a esquerda.')

    if(rodando==True):
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n')) #segundo tiro
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO!') #caso acerte troca a condição pra False e para as checagens
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('Tente Novamente até acabar suas balas.')
                    print('O marciano está mais a direita')
                elif(valor1<valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('Tente Novamente até acabar suas balas.')
                    print('O marciano está mais a esquerda')

    if(rodando==True):   
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n')) #terceiro tiro
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO! Game Over.') #caso acerte troca a condição pra False e para as checagens
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('Tente Novamente até acabar suas balas.')
                    print('O marciano está mais a direita')
                elif(valor1<valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('Tente Novamente até acabar suas balas.')
                    print('O marciano está mais a esquerda')
                        
    if(rodando==True):
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n')) #quarto tiro
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO! Game Over.') #caso acerte troca a condição pra False e para as checagens
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('Tente Novamente até acabar suas balas.')
                    print('O marciano está mais a direita')
                elif(valor1<valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('Tente Novamente até acabar suas balas.')
                    print('O marciano está mais a esquerda')

    if(rodando==True):
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n')) #quinto tiro
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO!') #caso acerte troca a condição pra False e para as checagens
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print('\nVocê errou.Você não tem mais balas.')
                    print('O marciano estava mais a direita. Você foi levado para Marte! \n Game Over.')
                elif(valor1<valor2):
                    balas-=1
                    print('\nVocê errou.Você não tem mais balas.')
                    print('O marciano estava mais a esquerda. Você foi levado para Marte! \n Game Over.')
    else:
        print("\n Game Over.")