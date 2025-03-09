from pulp import *

# Criar o modelo de programação inteira
model = LpProblem("Branch_and_Bound_Problem", LpMaximize)

# Definir as variáveis inteiras
x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')

# Definir a função objetivo
model += 3*x1 + 5*x2

# Definir as restrições
model += 2*x1 + 4*x2 <= 25
model += x1 <= 8
model += 2*x2 <= 10

# Resolver o modelo
model.solve()

# Verificar o status da solução
if LpStatus[model.status] == 'Optimal':
    print("Solução ótima encontrada!")
    print(f"Objetivo = {value(model.objective)}")
    print(f"x1 = {value(x1)}, x2 = {value(x2)}")
else:
    print("A solução não é ótima ou não é viável.")
