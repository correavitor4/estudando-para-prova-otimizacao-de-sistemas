from pulp import *

model = pulp.LpProblem('linear_programming', LpMaximize)

# Aqui eu removi os upbound
x1 = LpVariable('x1', lowBound=0, cat='continuous')
x2 = LpVariable('x2', lowBound=0, cat='continuous')

model += 100*x1 + 150*x2

# Restrições
model += 8000*x1 + 4000*x2 <= 40000
model += 15*x1 + 30*x2 <= 200


# restrições dos ramos da árvore (ir modificando à medida em que vai avançando nos ramos)
model += x2 >= 6
model += x1 >= 2


#solve
results = model.solve()

# print results
if LpStatus[results] == 'Optimal': print('The solution is optimal.')
else: print('\033[33mThe solution is not optimal\033[0m')
print(f'Objective value: z* = {value(model.objective)}')
print(f'Solution: \nx1* = {value(x1)},\n x2* = {value(x2)}')