import os

restaurantes = [
    {'nome': 'Restaurante 1', 'categoria': 'opção 1', 'ativo': True}, 
    {'nome': 'Restaurante 2', 'categoria': 'opção 2', 'ativo': True}
]

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    '''Exibe as opções do menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

# por padrão o input retorna uma string

def voltar_ao_menu_principal():
    input('Pressione qualquer tecla para voltar ao menu principal...')
    main()

def finalizar_app():
    exibir_subtitulo('Saindo...\n')

def opcoe_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * (len(subtitulo) + 4)
    print(linha)
    print(subtitulo)
    print(linha)

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante: {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_reaturantes():
    exibir_subtitulo('Lista de restaurantes\n')
    for restaurante in restaurantes:
        print(f' -> {restaurante.get('nome')} | {restaurante.get('categoria')} | {restaurante.get('ativo')}\n')
    print()
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo('Alternar estado do restaurante\n')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar status: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Digite uma opção: '))
        print(f'você escolheu a opção: {opcao_escolhida}!')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_reaturantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcoe_invalida()
    except:
        opcoe_invalida()

def main():
    exibir_subtitulo('')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
