# Importa o módulo "os", usado para limpar o terminal
import os

# Lista que guarda todas as tarefas 
# Cada tarefa é um dicionário
tarefas = []

# mantém o menu aparecendo até o usuário escolher "Sair"
while True:
    # Mostra o menu de opções
    print('----- MENU -----')
    print('1. Adicionar Tarefa')
    print('2. Ver ou Listar Tarefas')
    print('3. Marcar tarefa como concluída')
    print('4. Remover Tarefa')
    print('5. Sair')
    print("-"*16) 

    # Lê a opção escolhida 
    opcao = input('Digite uma opção: ')

    # Limpa o terminal: "cls" no Windows, "clear" no Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")

    # ---------- OPÇÃO 1: ADICIONAR TAREFA ----------
    if opcao == '1':
        titulo = input('Qual o titulo da tarefa: ')
        # Cria o dicionário da tarefa; toda tarefa nova começa como não concluída
        nova_tarefa = {"titulo": titulo, "concluida": False}
        # Adiciona a tarefa na lista
        tarefas.append(nova_tarefa)
        print(f'A tarefa "{titulo}" foi adicionada a lista!')

    # ---------- OPÇÃO 2: LISTAR TAREFAS ----------
    elif opcao == '2':
        # verifica se tem tarefas na lista
        if not tarefas:
            print('Nenhuma tarefa adicionada!')
        else:
            # enumerate devolve o índice e a tarefa a cada volta
            for indice, tarefa in enumerate(tarefas):
                status = "[X]" if tarefa['concluida'] else "[ ]"
                # indice + 1 para o usuário ver a contagem começando em 1
                print(f'{indice + 1}. {status} {tarefa["titulo"]}')

    # ---------- OPÇÃO 3: MARCAR COMO CONCLUÍDA ----------
    elif opcao == '3':
        if not tarefas:
            print('Nenhuma tarefa para concluir!')
        else:
            # Mostra a lista para o usuário escolher qual tarefa concluir
            for indice, tarefa in enumerate(tarefas):
                status = "[X]" if tarefa['concluida'] else "[ ]"
                print(f'{indice + 1}. {status} {tarefa["titulo"]}')

            # Converte para int, pois vamos usar o número para acessar a lista
            numero = int(input('Qual tarefa deseja concluir: '))

            # Valida se o número está entre 1 e a quantidade de tarefas
            if 1 <= numero <= len(tarefas):
                # numero - 1 porque a lista começa no índice 0
                # Altera o valor da chave "concluida" desse dicionário para True
                tarefas[numero - 1]["concluida"] = True
                print('Tarefa Concluída!')
            else:
                print('Numero inválido')

    # ---------- OPÇÃO 4: REMOVER TAREFA ----------
    elif opcao == '4':
        if not tarefas:
            print('Nenhuma tarefa para remover!')
        else:
            # Mostra a lista para o usuário escolher qual tarefa remover
            for indice, tarefa in enumerate(tarefas):
                status = "[X]" if tarefa['concluida'] else "[ ]"
                print(f'{indice + 1}. {status} {tarefa["titulo"]}')

            numero = int(input('Qual tarefa você quer remover: '))

            # Valida se o número existe na lista
            if 1 <= numero <= len(tarefas):
                # pop() remove o item da posição indicada e devolve o item removido
                tarefa_removida = tarefas.pop(numero - 1)
                print(f"Tarefa '{tarefa_removida['titulo']}' removida!")
            else:
                print('Número invalido!')

    # ---------- OPÇÃO 5: SAIR ----------
    elif opcao == "5":
        print('Saindo...')
        break  # Encerra o while e finaliza o programa

    # ---------- QUALQUER OUTRA ENTRADA ----------
    else:
        print('Opção inválida! Digite novamente.')

    # Pausa para o usuário conseguir ler o resultado antes de a tela ser limpa
    # (não roda na opção 5, porque o break já saiu do loop)
    input('\nPressione Enter para continuar...')
    os.system("cls" if os.name == "nt" else "clear")