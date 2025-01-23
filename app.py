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
    exibir_subtitulo('Finalizando o app.\n')

def volta_menu():
    input('\nPressione ENTER para voltar ao menu principal. ')
    main() ## Reinicia o programa

def opcao_invalida():
    print('\nOpção inválida.\n')
    volta_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'\n{texto}\n')

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Nome do restaurante: ')
    restaurantes.append(nome_restaurante) ## Adiciona o nome do restaurante à lista
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    volta_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes:')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
        
    volta_menu()
        

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

