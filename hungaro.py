import numpy as np
from scipy.optimize import linear_sum_assignment

# Esse é o exemplo que está no Slide "slide_4-1_metodo_hungaro" na página 29 de 30
cost_matrix = np.array([
    [90, 75, 75, 80],
    [35, 85, 55, 65],
    [125, 95, 90, 105],
    [45, 110, 95, 115]
])

# Resolver o problema usando o algoritmo húngaro
row_ind, col_ind = linear_sum_assignment(cost_matrix)

# Mostrar o resultado
print(f"Índices das linhas atribuídos: {row_ind}")
print(f"Índices das colunas atribuídos: {col_ind}")
print(f"Custo mínimo: {cost_matrix[row_ind, col_ind].sum()}")
