
import datetime

eventos = {}  # Armazena eventos com chave sendo o nome
inscricoes = {}  # Armazena listas de inscritos por evento

def cadastrar_evento():
    nome = input("Nome do evento: ").strip()
    if nome in eventos:
        print("Evento já cadastrado.")
        return
    data = input("Data do evento (DD/MM/AAAA): ").strip()
    descricao = input("Descrição: ").strip()
    try:
        vagas = int(input("Número máximo de participantes: "))
        eventos[nome] = {
            "data": data,
            "descricao": descricao,
            "vagas": vagas,
            "inscritos": []
        }
        print("Evento cadastrado com sucesso!")
    except ValueError:
        print("Número de vagas inválido.")

def atualizar_evento():
    nome = input("Nome do evento a atualizar: ").strip()
    if nome not in eventos:
        print("Evento não encontrado.")
        return
    data = input("Nova data (ou Enter para manter atual): ").strip()
    vagas_input = input("Novo número de vagas (ou Enter para manter atual): ").strip()
    if data:
        eventos[nome]["data"] = data
    if vagas_input:
        try:
            vagas = int(vagas_input)
            if vagas < len(eventos[nome]["inscritos"]):
                print("Não é possível reduzir vagas abaixo do número de inscritos.")
            else:
                eventos[nome]["vagas"] = vagas
        except ValueError:
            print("Valor inválido para vagas.")
    print("Evento atualizado!")

def visualizar_eventos():
    if not eventos:
        print("Nenhum evento disponível.")
        return
    print("\n--- EVENTOS DISPONÍVEIS ---")
    for nome, dados in eventos.items():
        vagas_restantes = dados["vagas"] - len(dados["inscritos"])
        print(f"Nome: {nome}\nData: {dados['data']}\nDescrição: {dados['descricao']}\nVagas restantes: {vagas_restantes}\n")

def inscrever_em_evento():
    nome = input("Nome do evento para inscrição: ").strip()
    if nome not in eventos:
        print("Evento não encontrado.")
        return
    if len(eventos[nome]["inscritos"]) >= eventos[nome]["vagas"]:
        print("Evento lotado.")
        return
    participante = input("Nome do participante: ").strip()
    if participante in eventos[nome]["inscritos"]:
        print("Você já está inscrito neste evento.")
        return
    eventos[nome]["inscritos"].append(participante)
    print("Inscrição realizada com sucesso!")

def visualizar_inscricoes():
    nome = input("Nome do evento para ver inscritos: ").strip()
    if nome not in eventos:
        print("Evento não encontrado.")
        return
    inscritos = eventos[nome]["inscritos"]
    print(f"Inscritos no evento '{nome}':")
    if not inscritos:
        print("Nenhum inscrito ainda.")
    else:
        for pessoa in inscritos:
            print("-", pessoa)

def excluir_evento():
    nome = input("Nome do evento a excluir: ").strip()
    if nome in eventos:
        del eventos[nome]
        print("Evento excluído com sucesso.")
    else:
        print("Evento não encontrado.")

def menu():
    while True:
        print("\n===== MENU DE EVENTOS =====")
        print("1. Cadastrar Evento")
        print("2. Atualizar Evento")
        print("3. Visualizar Eventos")
        print("4. Inscrever-se em Evento")
        print("5. Ver Inscritos de um Evento")
        print("6. Excluir Evento")
        print("7. Sair")
        opcao = input("Escolha uma opção (1-7): ")

        if opcao == "1":
            cadastrar_evento()
        elif opcao == "2":
            atualizar_evento()
        elif opcao == "3":
            visualizar_eventos()
        elif opcao == "4":
            inscrever_em_evento()
        elif opcao == "5":
            visualizar_inscricoes()
        elif opcao == "6":
            excluir_evento()
        elif opcao == "7":
            print("Saindo do sistema de eventos...")
            break
        else:
            print("Opção inválida.")

menu()
