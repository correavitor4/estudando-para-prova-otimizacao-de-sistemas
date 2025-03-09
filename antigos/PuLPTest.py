from pulp import *

model = pulp.LpProblem('linear_programming', LpMaximize)

solver = getSolver('PULP_CBC_CMD')

x1 = LpVariable('x1', lowBound=0, cat='continuous')
x2 = LpVariable('x2', lowBound=0, cat='continuous')
x3 = LpVariable('x3', lowBound=0, cat='continuous')
x4 = LpVariable('x4', lowBound=0, cat='continuous')

model += 40*x1 + 36*x2 + 15*x3 + 10*x4

# Restrições
model += 12*x1 + 10*x2 + 5*x3 + 10*x4 <= 32
model += x2 <= 3
model += x1 <= 0
model += x3 >= 1
model += x2 <= 2

#solve
results = model.solve()

# print results
if LpStatus[results] == 'Optimal': print('The solution is optimal.')
else: print('\033[33mThe solution is not optimal\033[0m')
print(f'Objective value: z* = {value(model.objective)}')
print(f'Solution: \nx1* = {value(x1)},\n x2* = {value(x2)},\n x3 = {value(x3)},\n x4 = {value(x4)}')