# Testar uma decisão ou cenário

from calculos import calcular_maior, calcular_media
from kit_dados import modulos, leituras_ambientais, tripulacao, consumo_modulos, historico_apollo_superficie

print()
resposta = input("CONSEGUIMOS EXPANDIR FUNCIONÁRIOS? (s/n)")
print()

if resposta.lower() == "s":
    for modulo in modulos:
        if modulo["ocupacao"] +1 <= modulo["capacidade"]:
            print(modulo["nome"], "- Capaz de contratar mais funcionários", "- Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"])
        else:
            print(modulo["nome"], "- Capacidade crítica, não contratar", "- Capacidade:", modulo["capacidade"], "- Ocupação:", modulo["ocupacao"])

