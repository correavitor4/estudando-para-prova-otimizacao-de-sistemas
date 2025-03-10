import numpy as np
from scipy.optimize import linear_sum_assignment

# Esse é o exemplo que está no Slide "slide_4-1_metodo_hungaro" na página 29 de 30
cost_matrix = np.array([
    [20, 25, 22, 28],
    [15, 18, 23, 17],
    [19, 17, 21, 24],
    [25, 23, 24, 24]
])

# Resolver o problema usando o algoritmo húngaro
row_ind, col_ind = linear_sum_assignment(cost_matrix)

# Mostrar o resultado
print(f"Índices das linhas atribuídos: {row_ind}")
print(f"Índices das colunas atribuídos: {col_ind}")
print(f"Custo mínimo: {cost_matrix[row_ind, col_ind].sum()}")
