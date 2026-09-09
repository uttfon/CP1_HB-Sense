def calcular_media(valores):
    return sum(valores) / len(valores)

def calcular_maior(valores):
    return max(valores)

def analisar_mapa_base(mapa):
    total_livres = 0
    total_ocupados = 0
    total_restritos = 0

    for linha in mapa:
        for setor in linha:
            if setor == 0:
                total_livres += 1
            elif setor == 1:
                total_ocupados += 1
            elif setor == 2:
                total_restritos += 1

    total_setores = total_livres + total_ocupados + total_restritos
    pct_restrito = (total_restritos / total_setores) * 100

    return total_livres, total_ocupados, total_restritos, pct_restrito

def classificar_modulo(capacidade, ocupacao):
    vagas = capacidade - ocupacao
    if vagas <= 0:
        return "CRÍTICO"
    elif vagas == 1:
        return "ATENÇÃO"
    else:
        return "APTO A EXPANSÃO"

def classificar_ciclo_ambiental(o2_pct, co2_ppm, temp_c, limites):
    o2_minimo, co2_maximo, temp_maxima = limites

    if o2_pct < o2_minimo or co2_ppm >= co2_maximo:
        return "CRÍTICO", "Nível de O2 ou CO2 fora da faixa segura"
    elif co2_ppm >= co2_maximo * 0.85 or temp_c >= temp_maxima:
        return "ATENÇÃO", "Tendência de degradação do ar ou temperatura elevada"
    else:
        return "NORMAL", "Parâmetros dentro da faixa esperada"

