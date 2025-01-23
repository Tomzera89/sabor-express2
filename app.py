import os

restaurantes = ['Orly', 'Kieza']

def exibir_nome_programa():
    print ("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('\nFinalizando o app.\n')

def opcao_invalida():
    print('\nOpção inválida.\n')
    input('Pressione ENTER para voltar ao menu principal.')
    main() ## Reinicia o programa

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastrando novo restaurante...')
    nome_restaurante = input('Nome do restaurante: ')
    restaurantes.append(nome_restaurante) ## Adiciona o nome do restaurante à lista
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    input('\nPressione ENTER para voltar ao menu principal.')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes:\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
        
    input('\nPressione ENTER para voltar ao menu principal.')
    main()
        


def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Digite a opção desejada: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('\nAtivando restaurante...')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')  # Limpa a tela no Windows
    exibir_nome_programa()
    menu()
    escolher_opcao()

if __name__ == '__main__':
    main()


## parei no tópico 'Lista, laços e exceções,aula 07'