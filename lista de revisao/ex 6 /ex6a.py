from pulp import *

model = pulp.LpProblem('linear_programming', LpMaximize)

# Aqui eu removi os upbound
x1 = LpVariable('x1', lowBound=0, cat='continuous')
x2 = LpVariable('x2', lowBound=0, cat='continuous')

model += 3*x1 + 5*x2

# Restrições
model += 2*x1 + 4*x2 <= 25
model += x1 <= 8
model += 2*x2 <= 10



# restrições dos ramos da árvore (ir modificando à medida em que vai avançando nos ramos)
model += x2 >= 3
model += x1 >= 7


#solve
results = model.solve()

# print results
if LpStatus[results] == 'Optimal': print('The solution is optimal.')
else: print('\033[33mThe solution is not optimal\033[0m')
print(f'Objective value: z* = {value(model.objective)}')
print(f'Solution: \nx1* = {value(x1)},\n x2* = {value(x2)}')