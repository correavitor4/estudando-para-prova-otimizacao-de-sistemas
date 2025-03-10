import numpy as np


def canto_noroeste(oferta, demanda):
    oferta = oferta.copy()
    demanda = demanda.copy()

    linhas, colunas = len(oferta), len(demanda)
    alocacao = np.zeros((linhas, colunas), dtype=int)

    i, j = 0, 0
    while i < linhas and j < colunas:
        aloca = min(oferta[i], demanda[j])
        alocacao[i][j] = aloca
        oferta[i] -= aloca
        demanda[j] -= aloca

        if oferta[i] == 0:
            i += 1
        if demanda[j] == 0:
            j += 1

    return alocacao


# Dados do problema
custos = np.array([
    [6, 5, 8],
    [13, 12, 1],
    [7, 9, 5],
    [10, 6, 4]
])

oferta = [10, 20, 12, 13]
demanda = [8, 30, 15]

# Solução usando o método do Canto Noroeste
alocacao = canto_noroeste(oferta, demanda)
custo_total = np.sum(alocacao * custos)

print("Alocação:\n", alocacao)
print("Custo Total:", custo_total)


def custo_minimo(oferta, demanda, custos):
    oferta = np.array(oferta)
    demanda = np.array(demanda)
    custos = custos.astype(float)  # Converter custos para float

    linhas, colunas = custos.shape
    alocacao = np.zeros((linhas, colunas), dtype=int)

    while np.any(oferta > 0) and np.any(demanda > 0):
        i, j = np.unravel_index(np.argmin(custos), custos.shape)
        aloca = min(oferta[i], demanda[j])
        alocacao[i, j] = aloca

        oferta[i] -= aloca
        demanda[j] -= aloca

        if oferta[i] == 0:
            custos[i, :] = np.inf  # Agora custos é float, então isso funciona
        if demanda[j] == 0:
            custos[:, j] = np.inf

    return alocacao


# Solução usando o método do Custo Mínimo
alocacao = custo_minimo(oferta, demanda, custos.copy())
custo_total = np.sum(alocacao * custos)

print("Alocação:\n", alocacao)
print("Custo Total:", custo_total)


def vogel(oferta, demanda, custos):
    oferta = np.array(oferta, dtype=int)  # Converter para array NumPy
    demanda = np.array(demanda, dtype=int)
    custos = custos.copy().astype(float)  # Evitar problemas com np.inf

    linhas, colunas = custos.shape
    alocacao = np.zeros((linhas, colunas), dtype=int)

    while np.any(oferta > 0) and np.any(demanda > 0):
        # Calcular penalidades
        def calcular_penalidade(mat):
            penalidades = []
            for row in mat:
                valores = sorted([v for v in row if v != np.inf])
                if len(valores) > 1:
                    penalidades.append(valores[1] - valores[0])
                elif valores:
                    penalidades.append(valores[0])
                else:
                    penalidades.append(-1)
            return penalidades

        # Penalidades das linhas e colunas
        linha_penalidades = calcular_penalidade(custos)
        coluna_penalidades = calcular_penalidade(custos.T)

        # Escolher a linha ou coluna com maior penalidade
        if max(linha_penalidades) >= max(coluna_penalidades):
            i = np.argmax(linha_penalidades)
            j = np.argmin(custos[i])
        else:
            j = np.argmax(coluna_penalidades)
            i = np.argmin(custos[:, j])

        # Alocar oferta e demanda
        aloca = min(oferta[i], demanda[j])
        alocacao[i, j] = aloca
        oferta[i] -= aloca
        demanda[j] -= aloca

        # Marcar linha ou coluna como completa
        if oferta[i] == 0:
            custos[i, :] = np.inf
        if demanda[j] == 0:
            custos[:, j] = np.inf

    return alocacao



# Solução usando o método de Vogel
alocacao = vogel(oferta, demanda, custos.copy())
custo_total = np.sum(alocacao * custos)

print("Alocação:\n", alocacao)
print("Custo Total:", custo_total)
