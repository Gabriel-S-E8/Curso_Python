def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"Tarefa": nome_tarefa, "Completada": False}
    
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso! ")
    return

def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["Completada"] else " "
    nome_tarefa = tarefa["Tarefa"]
    print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    tarefas[indice_tarefa_ajustado]["Tarefa"] = novo_nome_tarefa
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
  else:
    print("Índice de tarefas inválido.")
  return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    tarefas[indice_tarefa_ajustado]["Completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["Completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas.")
    return

tarefas = []
while True:
    print("\n Menu do Gerenciador de lista de tarefas: ")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")

    escolha = input("Digite a opção desejada: ")
    
    match escolha:
        case "1":
            nome_tarefa = input("Qual o nome da tarefa que deseja cadastrar? ")
            adicionar_tarefa(tarefas, nome_tarefa)
        case "2":
            ver_tarefas(tarefas)
        case "3":
            ver_tarefas(tarefas)
            indice_tarefa = input('Digite o numero da tarefa que deseja atualizar: ')
            if int(indice_tarefa)>=0 and int(indice_tarefa)<=len(tarefas):
                novo_nome = input('Digite o novo nome da tarefa: ')
                atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome) 
            else:
                print('Tarefa não encontrada ou invalida.')
        case "4":
            ver_tarefas(tarefas)
            indice_tarefa = input("Digite o numero da tarefa que deseja completar.")
            if int(indice_tarefa)>=0 and int(indice_tarefa)<=len(tarefas):
                completar_tarefa(tarefas, indice_tarefa)
            else:
                print('Tarefa não encontrada ou invalida.')
        case "5":
            deletar_tarefas_completadas(tarefas)
            ver_tarefas(tarefas)
        case "6":
            print("Programa Finalizado")
            break
        case _:
            print("Opção inválida. Tente novamente.")
            
            
print("Programa Finalizado")
