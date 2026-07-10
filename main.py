import json
def menu_charmoso():
    print('═' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('═' * 40)
    print('COMANDOS'.center(40))
    print('-' * 40)
    print('» Adicionar jogos [ADD]')
    print('» Lista de jogos [LIST]')
    print('» Atualizar Jogo [UPDATE]')
    print('» Deletar Jogo [DELETE]')
    print('» Sobre [ABOUT]')
    print('» Sair [QUIT]')
    print('-' * 40)

def carregar_arquivos():
    #Carrega os jogos do arquivo JSON.
    try:
        with open('biblioteca jogos.json', 'r') as arquivo_jogos:
            dados_jogos = json.load(arquivo_jogos)
            return dados_jogos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('═' * 40)
        print('Arquivo JSON vazio ou corrompido.'.center(40))
        print('Iniciando biblioteca vazia'.center(40))
        return []

def salvar_arquivos(lista):
    with open('biblioteca jogos.json', 'w') as arquivo_jogos:
        json.dump(lista,arquivo_jogos,  indent=4)

def apenas_sim_ou_nao(nome_jogo):
    while True:
        sim_nao = input(f'> Você terminou {(nome_jogo)}? (sim/não):')
        if not sim_nao in ('sim', 'nao', 'não'):
            print('┉' * 40)
            print('Use apenas sim ou não'.center(40))
            print('┉' * 40)
        elif sim_nao == 'sim':
            sim_nao = True
            break
        elif sim_nao == 'nao' or sim_nao == 'não':
            sim_nao = False
            break
    return sim_nao

def encontrar_jogos(lista,jogo_encontrado):
    for dicionario_jogos in lista:
        if dicionario_jogos['nome jogo'].lower() == jogo_encontrado.lower():
            return dicionario_jogos
    else:
        return None

def adicionar_jogos(lista):
    print('═' * 40)
    print('ADICIONAR JOGOS'.center(40))
    print('═' * 40)
    while True:
        try:
            add = int(input('> Quantos jogos deseja adicionar?:'))
            print('─' * 40)
            if add < 1:
                print('┉' * 40)
                print('NÚMERO INVÁLIDO, TENTE NOVAMENTE'.center(40))
                print('┉' * 40)
            else:
                for i in range(add):
                    while True:
                        nome_jogo = (input(f'> [{str(i + 1)}] Nome do Jogo:'))
                        if encontrar_jogos(lista, nome_jogo):
                            print('┉' * 40)
                            print('ESSE JOGO JÁ ESTÁ NA LISTA'.center(40))
                            print('Digite outro jogo'.center(40))
                            print('┉' * 40)
                        else:
                            sim_nao = apenas_sim_ou_nao(nome_jogo)
                            dicionario_jogos = {
                                'nome jogo': nome_jogo,
                                'concluido': sim_nao,
                                'historico': []
                            }
                            lista.append(dicionario_jogos)
                            print(f'> {nome_jogo} adicionado a biblioteca')
                            print('─'*40)
                            break

                break
        except ValueError:
            print('┉' * 40)
            print('INSIRA UM NÚMERO'.center(40))
            print('┉' * 40)

def lista_jogos(lista):
    if not lista:
        print('═' * 40)
        print('SUA LISTA ESTÁ VAZIA'.center(40))
        print('═' * 40)
    else:
        print('═' * 40)
        print('SUA LISTA'.center(40))
        print('═' * 40)
        for dicionario_jogos in lista:
            if dicionario_jogos['concluido']:
                status = 'Concluído'
            else:
                status = 'Não concluído'
            print(f"► {dicionario_jogos['nome jogo']}")
            print(f" └─{status} ")
            for alteracao in dicionario_jogos['historico']:
                print(f"  └─{alteracao}")
        print('─' * 40)

def sobre():
    print('═' * 40)
    print('SOBRE'.center(40))
    print('═' * 40)
    print('Biblioteca de jogos'.center(40))
    print('Feito por: João Gabriel Lara'.center(40))
    print('-' * 40)
    print('Para gerenciar sua coleção de jogos'.center(40))
    print('-' * 40)

def update_lista(lista):
    print('═' * 40)
    print('ATUALIZAR JOGOS'.center(40))
    print('═' * 40)
    print('Para retornar ao menu principal'.center(40))
    print('Digite: sair'.center(40))
    print('─' * 40)
    while True:
        if not lista:
            print('-' * 40)
            print('NÃO EXISTE NENHUM JOGO NA LISTA'.center(40))
            print('-' * 40)
            print('─' * 40)
            print('RETORNANDO AO MENU PRINCIPAL...'.center(40))
            print('─' * 40)
            break
        nome_jogo = (input('> Qual jogo deseja atualizar?:'))
        jogo_update = encontrar_jogos(lista,nome_jogo)
        if nome_jogo.lower() == 'sair':
            print('─' * 40)
            print('RETORNANDO AO MENU PRINCIPAL...'.center(40))
            print('─' * 40)
            break
        elif jogo_update is None:
            print('-' * 40)
            print('ESSE JOGO NÃO ESTÁ LISTADO'.center(40))
            print('-' * 40)

        else:
            sim_nao = apenas_sim_ou_nao(nome_jogo)
            jogo_update['concluido'] = sim_nao
            print(f"> {jogo_update['nome jogo']} alterado com sucesso")
            print('─' * 40)
            hoje = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
            if sim_nao:
                tupla_jogos = ('Concluído', hoje)
                jogo_update['historico'].append(tupla_jogos)
                break
            else:
                tupla_jogos = ('Não concluído', hoje)
                jogo_update['historico'].append(tupla_jogos)
                break

def deletar_jogo(lista):
    print('═' * 40)
    print('DELETAR JOGOS'.center(40))
    print('═' * 40)
    print('Para retornar ao menu principal'.center(40))
    print('Digite: sair'.center(40))
    print('─' * 40)
    while True:
        jogo_encontrado = (input('> Qual jogo deseja deletar?:'))
        jogo_deletado = encontrar_jogos(lista,jogo_encontrado)
        if jogo_encontrado.lower() == 'sair':
            print('─' * 40)
            print('RETORNANDO AO MENU PRINCIPAL...'.center(40))
            print('─' * 40)
            break
        elif jogo_deletado:
            lista.remove(jogo_deletado)
            print(f'> {jogo_encontrado} foi deletado com sucesso')
            print('─' * 40)
            break
        elif jogo_deletado is None:
            print('-' * 40)
            print('ESSE JOGO NÃO ESTÁ LISTADO'.center(40))
            print('-' * 40)
            if not lista:
                break

def sair(lista):
    print('═' * 40)
    print('FINALIZANDO BIBLIOTECA DE JOGOS...'.center(40))
    print('═' * 40)
    salvar_arquivos(lista)

from datetime import datetime
lista = carregar_arquivos()
menu_charmoso()

while True:
    comando = input('> Digite um comando:').lower()
    if comando == 'about':
        sobre()

    elif comando == 'add':
        adicionar_jogos(lista)

    elif comando == 'list':
        lista_jogos(lista)

    elif comando == 'update':
        update_lista(lista)

    elif comando == 'delete':
        deletar_jogo(lista)

    elif comando == 'quit':
        sair(lista)
        break

    else:
        print('┉'*40)
        print('COMANDO INVÁLIDO'.center(40))
        print('Por favor, verifique a lista de comandos'.center(40))
        print('┉' * 40)
