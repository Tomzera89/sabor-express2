import os

restaurantes = [{'nome': 'Orly', 'categoria': 'Padaria', 'ativo': False},
                {'nome': 'Kieza', 'categoria': 'Churrascaria', 'ativo': True},
                {'nome': 'Casa da Mãe', 'categoria': 'Fast-Food', 'ativo': False}
]

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
    print('3. Ativar ou desativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app.')

def volta_menu():
    input('\nPressione ENTER para voltar ao menu principal. ')
    main() ## Reinicia o programa

def opcao_invalida():
    print('\nOpção inválida.\n')
    volta_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '#' * (len(texto)) # Cria uma linha com o mesmo número de caracteres do texto
    print(linha)
    print(f'{texto}')
    print(linha)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Nome do restaurante: ')
    categoria_restaurante = input(f'Categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)  # Adiciona o novo restaurante à lista
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    volta_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes:')

    print(f'|{"Nome".ljust(15)}|{"Categoria".ljust(15)}|{"Status"}')
    print(f'+{"-" * 15}+{"-" * 15}+{"-" * 10}\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'|{nome_restaurante.ljust(15)}|{categoria_restaurante.ljust(15)}|{ativo_restaurante}')
        
    volta_menu()
        
def alternar_ativacao_restaurante():
    exibir_subtitulo('Ativar/Desativar restaurante')
    nome_restaurante = input('Nome do restaurante: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'Restaurante {nome_restaurante} foi {restaurante["ativo"] and "ativado" or "desativado"} com sucesso!'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.')

        
    volta_menu()


def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Digite a opção desejada: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_ativacao_restaurante()
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

