from time import sleep
from os import system

def voltando_menu():
    print('Voltando...')
    sleep(2)
    system('cls')

def menu(inserir_dados, listar_carros, buscar_carros):
    while True:
        print('Olá, seja bem-vindo a Volvo!')
        print('O que você quer fazer hoje?\n1. Inserir novos carros\n2. Listar carros\n3. Buscar carros\n4. Sair')
        opcao = int(input(''))

        if opcao == 1:
            while True:
                tipo = str(input('Digite o tipo de carro: ')).upper()
                ano = int(input('Digite o ano do carro: '))
                qtd_portas = int(input('Digite a quantidade de portas: '))
                potencia = int(input('Digite a potencia do carro: '))
                inserir_dados(tipo, ano, qtd_portas, potencia)
                while True:
                    opcao = int(input('Deseja adicionar outro carro?\n1. Sim\n2. Não\n'))
                    if opcao == 1:
                        break
                    elif opcao == 2:
                        voltando_menu()
                        return menu(inserir_dados, listar_carros, buscar_carros)
                    else:
                        print('Opção incorreta!')
                        sleep(1)
                    
                
        elif opcao == 2:
            listar_carros()
            sleep(2)
        
        elif opcao == 3:
            while True:
                tipo = str(input('Digite o tipo de carro para a consulta: ')).upper()
                buscar_carros(tipo)
                while True:
                    opcao = int(input('Deseja realizar outra consulta?\n1. Sim\n2. Não\n'))
                    if opcao == 1:
                        break
                    if opcao == 2:
                        voltando_menu()
                        return menu(inserir_dados, listar_carros, buscar_carros)
                    else:
                        print('Opção incorreta!')
                        sleep(1)
                
        elif opcao == 4:
            print('Saindo...')
            sleep(2)
            system('cls')
            break
            
        else:
            print('Opção incorreta!')
            sleep(1)
            system('cls')