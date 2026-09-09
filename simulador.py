# Testar uma decisão ou cenário

from calculos import calcular_maior, calcular_media, classificar_modulo
from kit_dados import modulos, leituras_ambientais, tripulacao, consumo_modulos, historico_apollo_superficie

print("==== GERENCIAMENTO DE RESIDÊNCIA E BASE ====")

opcao = 0

while opcao != 4:

    print()
    print("1 - Expandir funcionários?")
    print("2 - Precisamos de manutenção?")
    print("3 - Problema de consumo de água?")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 4:
        print("Saindo do sistema...")
        break

    if opcao == 1:
        print()
        resposta = input("PRECISAMOS EXPANDIR FUNCIONÁRIOS? (s/n) ")
        print()
        print("==== EXPANSÃO DE FUNCIONÁRIOS ====")
        print()
        if resposta.lower() == "s":
            modulos_aptos = 0
            for modulo in modulos:
                status_modulo = classificar_modulo(modulo["capacidade"], modulo["ocupacao"])
                print(modulo["nome"])
                print("Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"])
                print("STATUS:", status_modulo)
                print()
                if status_modulo == "APTO A EXPANSÃO":
                    modulos_aptos += 1

            print("================")
            if modulos_aptos > 0:
                print("RESULTADO: EXPANSÃO AUTORIZADA")
                print("Recomendação:", modulos_aptos, "módulo(s) possuem vagas suficientes para receber novos tripulantes.")
            else:
                print("RESULTADO: EXPANSÃO NÃO RECOMENDADA")
                print("Recomendação: Nenhum módulo possui vagas suficientes no momento.")
            print("================")
        else:
            print("Nenhuma ação de expansão será realizada.")

    elif opcao == 2:
        print()
        turno = input("Qual o turno atual, A ou B? ").upper()
        while turno != "A" and turno != "B":
            turno = input("Digite um valor válido (A ou B)! ").upper()

        resposta_2 = input("PRECISAMOS FAZER MANUTENÇÃO NO PAINEL DE ENERGIA? (s/n) ")
        print()
        print("==== MANUTENÇÃO NO PAINEL DE ENERGIA ====")
        print()
        if resposta_2.lower() == "s":
            equipe_disponivel = 0
            for funcionarios in tripulacao:
                if (funcionarios["funcao"] == "Engenheira" or funcionarios["funcao"] == "Tecnico") and turno == "A":
                    print(funcionarios["funcao"], "- DISPONÍVEL PARA MANUTENÇÃO NO TURNO", turno)
                    equipe_disponivel += 1
                else:
                    print(funcionarios["funcao"], "- SEM EQUIPE NECESSÁRIA NO TURNO", turno)

            print()
            print("================")
            if equipe_disponivel > 0:
                print("RESULTADO: MANUTENÇÃO AUTORIZADA")
                print("Recomendação:", equipe_disponivel, "profissional(is) disponível(is) para realizar a manutenção agora.")
            else:
                print("RESULTADO: MANUTENÇÃO ADIADA")
                print("Recomendação: Aguardar o turno A, quando a equipe técnica está disponível.")
            print("================")
        else:
            print("Nenhuma manutenção será realizada.")

    elif opcao == 3:
        print()
        turno = input("Qual o turno atual, A ou B? ").upper()
        while turno != "A" and turno != "B":
            turno = input("Digite um valor válido (A ou B)! ").upper()

        resposta_3 = input("PRECISAMOS AUMENTAR O ABASTECIMENTO DE ÁGUA? (s/n) ")
        print()
        print("==== ABASTECIMENTO DE ÁGUA ====")
        print()
        if resposta_3.lower() == "s":
            comandante_disponivel = 0
            for funcionarios in tripulacao:
                if funcionarios["funcao"] == "Comandante" and turno == "A":
                    comandante_disponivel += 1

            print("================")
            if comandante_disponivel > 0:
                print("RESULTADO: COMANDANTE NOTIFICADO")
                print("Recomendação: Comandante em serviço no turno", turno, "- alerta de baixo nível de água enviado imediatamente.")
            else:
                print("RESULTADO: NOTIFICAÇÃO PENDENTE")
                print("Recomendação: Comandante fora de turno. Acionar substituto ou aguardar retorno ao turno A.")
            print("================")
        else:
            print("Nenhuma ação de abastecimento será realizada.")