from pulp import *

model = pulp.LpProblem('linear_programming', LpMinimize)

solver = getSolver('PULP_CBC_CMD')

x1 = LpVariable('x1', lowBound=0, upBound=1, cat='continuous')
x2 = LpVariable('x2', lowBound=0, upBound=1, cat='continuous')
x3 = LpVariable('x3', lowBound=0, upBound=1, cat='continuous')

model += 4*x1 + 3*x2 + 2*x3

# Restrições
model += 2*x1 + 2*x2 + 4*x3 >= 3.8
model += 3*x1 + 2*x2 + 4*x3 >= 6.6
model += 4*x1 + 3*x2 + 2*x3 >= 6.6

model += x2 == 20
model += x1 == 1
model += x3 == 1

#solve
results = model.solve()

# print results
if LpStatus[results] == 'Optimal': print('The solution is optimal.')
else: print('\033[33mThe solution is not optimal\033[0m')
print(f'Objective value: z* = {value(model.objective)}')
print(f'Solution: \nx1* = {value(x1)},\n x2* = {value(x2)},\n x3 = {value(x3)}')