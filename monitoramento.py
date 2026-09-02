# Entender a situação atual

from calculos import calcular_maior, calcular_media
from kit_dados import modulos, leituras_ambientais, tripulacao, consumo_modulos, historico_apollo_superficie

print("==== LEITURAS DE DADOS ====")

for modulo in modulos:
    print(modulo["nome"], "- Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"])

for leitura in leituras_ambientais:
    print("Ciclo", leitura["ciclo"], "- Porcentagem de O2:", leitura["o2_pct"], "%")

for pessoas in tripulacao:
    print("ID:", pessoas["id"], "- Turno:", pessoas["turno"])

for consumo in consumo_modulos:
    print("Módulo:", consumo["modulo"], "- Consumo de água:", consumo["agua_l_dia"], "- Consumo de energia:", consumo["energia_kwh_dia"])

for historico in historico_apollo_superficie:
    print("Missão:", historico["missao"], "- Horas de superfície:", historico["horas_superficie"])