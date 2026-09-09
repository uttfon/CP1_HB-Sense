# Entender a situação atual

from calculos import calcular_maior, calcular_media, classificar_modulo, classificar_ciclo_ambiental, analisar_mapa_base
from kit_dados import modulos, leituras_ambientais, tripulacao, consumo_modulos, historico_apollo_superficie, mapa_base
limites_seguranca = (20.0, 1000, 24.0)

print("==== LEITURAS DE DADOS ====")

print()
print("==== MÓDULOS ====")
for modulo in modulos:
    print(modulo["nome"], "- Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"], "- Energia diponível:", modulo["energia_kw"], "KW")
    status_modulo = classificar_modulo(modulo["capacidade"], modulo["ocupacao"])
    print("STATUS:", status_modulo)

print()
print("==== MAPA DA BASE ====")
livres, ocupados, restritos, pct_restrito = analisar_mapa_base(mapa_base)
print("Setores livres:", livres)
print("Setores ocupados:", ocupados)
print("Setores de acesso restrito:", restritos)
print("Percentual da base em acesso restrito:", pct_restrito, "%")

if pct_restrito >= 30:
    print("STATUS DA BASE: ALTA RESTRIÇÃO DE ÁREA")
elif pct_restrito >= 15:
    print("STATUS DA BASE: RESTRIÇÃO MODERADA")
else:
    print("STATUS DA BASE: ÁREA LIVRE ADEQUADA")

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

print()
print("==== CLASSIFICAÇÃO POR CICLO AMBIENTAL ====")
ciclo_mais_critico = 0

for leitura in leituras_ambientais:
    status_ciclo, motivo_ciclo = classificar_ciclo_ambiental(leitura["o2_pct"], leitura["co2_ppm"], leitura["temp_c"], limites_seguranca)
    print("Ciclo", leitura["ciclo"], "- STATUS:", status_ciclo, "-", motivo_ciclo)
    if status_ciclo == "CRÍTICO":
        ciclo_mais_critico = leitura["ciclo"]

print()
print("================")
if ciclo_mais_critico > 0:
    print("ALERTA: Ciclo", ciclo_mais_critico, "atingiu nível CRÍTICO de qualidade do ar. Recomenda-se intervenção imediata.")
else:
    print("Nenhum ciclo atingiu nível crítico. Operação dentro da normalidade.")
print("================")
print()