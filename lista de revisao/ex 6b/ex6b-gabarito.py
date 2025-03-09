from pulp import *

# Criar o modelo de maximização
model = pulp.LpProblem('linear_programming', LpMaximize)

# Definir as variáveis contínuas
# Variáveis inteiras
x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')


# Função objetivo
model += 100*x1 + 150*x2

# Restrições
model += 8000*x1 + 4000*x2 <= 40000  # Restrição de custo
model += 15*x1 + 30*x2 <= 200  # Restrição de capacidade

# Resolver o modelo
model.solve()

# Imprimir resultados
if LpStatus[model.status] == 'Optimal':
    print('The solution is optimal.')
else:
    print('\033[33mThe solution is not optimal\033[0m')

print(f'Objective value: z* = {value(model.objective)}')
print(f'Solution: \nx1* = {value(x1)},\n x2* = {value(x2)}')
