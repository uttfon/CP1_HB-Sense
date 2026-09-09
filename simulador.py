# Testar uma decisão ou cenário

import random
from calculos import calcular_maior, calcular_media
from kit_dados import modulos, leituras_ambientais, tripulacao, consumo_modulos, historico_apollo_superficie
print("==== GERENCIAMENTO DE RESIDÊNCIA E BASE ====")

opcao = 0

while opcao != 4:

    palavras = ["ALERTA DE MANUTENÇÃO NO MÓDULO MÉDICO", "ALERTA DE BAIXA EFICIÊNCIA DE TRABALHO", "ALERTA DE ALTO CONSUMO E BAIXO NÍVEL DE ÁGUA NO MÓDULO HB-06"]
    uma_palavra = random.choice(palavras)
    print()
    print(uma_palavra)

    print()
    print("1 - Expandir funcionários?")
    print("2 - Precisamos de manutenção?")
    print("3 - Problema de consumo de água?")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 4:
        print("Saindo do sistema...")
        break

    while True:
        turno = input("Qual o turno atual A ou B? ").upper()
        if turno == "A" or turno == "B":
            break

        print("Digite um valor válido (A e B)!")

    if turno.upper() == "A":
        print()
        print("==== TURNO A ====")

    elif turno.upper() == "B":
        print()
        print("==== TURNO B ====")
        
    else:
        print("Digie um turno válido A ou B")

    if opcao == 1:
        print()
        resposta = input("PRECISAMOS EXPANDIR FUNCIONÁRIOS? (s/n)")
        print()
        print("==== EXPANSÃO DE FUNCIONÁRIOS ====")
        print()
        if resposta.lower() == "s":
            for modulo in modulos:
                if modulo["ocupacao"] +1 < modulo["capacidade"]:
                    print(modulo["nome"])
                    print("Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"])
                    print("STATUS: APTO A EXPANSÃO")
                    print()

                elif modulo["capacidade"] +1 - modulo["ocupacao"] == 1:
                    print(modulo["nome"])
                    print("Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"])
                    print("STATUS: ATENÇÃO")
                    print()

                else:
                    print(modulo["nome"])
                    print("Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"])
                    print("STATUS: CRÍTICO")
                    print()

    elif opcao == 2:
        print()
        resposta_2 = input("PRECISAMOS FAZER MANUTENÇÃO NO PAINEL DE ENERGIA? (s/n)")
        print()
        if resposta_2.lower() == "s":
            for funcionarios in tripulacao:
                if funcionarios["funcao"] == "Engenheira" or "Tecnico" and funcionarios["turno"] == "A":
                    print(funcionarios["funcao"], "- TEMOS EQUIPE PARA REALIZAR A MANUTENÇÃO!")
                else:
                    print(funcionarios["funcao"], "- SEM EQUIPE NECESSÁRIA, ESPERAR PRÓXIMO TURNO")

    elif opcao == 3:
        print()
        resposta_3 = input("PRECISAMOS AUMENTAR O ABASTECIMENTO DE ÁGUA? (s/n)")
        print()
        if resposta_3.lower() == "s":
            for funcionarios in tripulacao:
                if funcionarios["funcao"] == "Comandante" and funcionarios["turno"] == "A":
                    print("COMANDANTE ALERTA SEVERO DE BAIXO H20 NO MÓDULO HB-06")
                else:
                    print("CHAMAR COMANDANTE IMEDITAMENTE")