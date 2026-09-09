# Entender a situação atual

import random
from calculos import calcular_maior, calcular_media
from kit_dados import modulos, leituras_ambientais, tripulacao, consumo_modulos, historico_apollo_superficie

print("==== LEITURAS DE DADOS ====")

print()
print("==== MÓDULOS ====")
for modulo in modulos:
    print(modulo["nome"], "- Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"], "- Energia diponível:", modulo["energia_kw"], "KW")
    if modulo["capacidade"] +1 - modulo["ocupacao"] == 1:
        print("STATUS: ATENÇÃO")
    elif modulo["ocupacao"] +1 < modulo["capacidade"]:
        print("STATUS: APTO A EXPANSÃO")
    else:
        print("STATUS: CRÍTICO")

print()
print("==== LEITURAS AMBIENTAIS ====")
for leitura in leituras_ambientais:
    print("Ciclo", leitura["ciclo"], "- Porcentagem de O2:", leitura["o2_pct"], "%", " - Temperatura externa", leitura["temp_c"], "°C")

temperaturas = [leitura["temp_c"] for leitura in leituras_ambientais]
media_temp = calcular_media(temperaturas)
maxima_temp = calcular_maior(temperaturas)

pct_02 = [leitura["o2_pct"] for leitura in leituras_ambientais]
media_o2 = calcular_media(pct_02)
maxima_o2 = calcular_maior(pct_02)

print()
print("Temperatura média -", media_temp, "°C")
print("Temperatura máxima registrada - ", maxima_temp, "°C")
print("Procentagem média de O2 - ", media_o2, "%")
print("Porcentagem máxima de O2 registrada -", maxima_o2, "%")

print()
print("==== TRIPULAÇÃO ====")
for pessoas in tripulacao:
    print("ID:", pessoas["id"], "- Módulo presente:", pessoas["modulo"], "- Função:", pessoas["funcao"])

print()
print("==== CONSUMO DOS MÓDULOS ====")
for consumo in consumo_modulos:
    print("Módulo:", consumo["modulo"], "- Consumo de água:", consumo["agua_l_dia"], "L - Consumo de energia:", consumo["energia_kwh_dia"])

consumo_agua = [consumo["agua_l_dia"] for consumo in consumo_modulos]
consumo_energia = [consumo["energia_kwh_dia"] for consumo in consumo_modulos]

media_consumo_agua = calcular_media(consumo_agua)
media_consumo_energia = calcular_media(consumo_energia)

print()
print("Consumo médio de água por dia - ", media_consumo_agua, "L")
print("Consumo médio de energia por dia - ", media_consumo_energia, "kwh")

print()
print("==== HISTÓRICO DE MISSÕES APOLLO ====")
for historico in historico_apollo_superficie:
    print("Missão:", historico["missao"], "- Horas de superfície:", historico["horas_superficie"])

tempo_superficie = [historico["horas_superficie"] for historico in historico_apollo_superficie]
media_horas = calcular_media(tempo_superficie)
maximo_horas = calcular_maior(tempo_superficie)

print()
print("Tempo médio de horas de superfície - ", media_horas, "horas")
print("Tempo máximo de horas de superfície - ", maximo_horas, "horas")

palavras = ["ALERTA DE MANUTENÇÃO NO PAINEL DE ENERGIA DO MÓDULO MÉDICO", "ALERTA DE BAIXA EFICIÊNCIA DE TRABALHO", "ALERTA DE ALTO CONSUMO E BAIXO NÍVEL DE ÁGUA NO MÓDULO HB-06"]
uma_palavra = random.choice(palavras)
print()
print("================")
print(uma_palavra)
print("================")
print()