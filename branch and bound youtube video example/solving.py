# Link para o vídeo: https://www.youtube.com/watch?v=1qmkb4Z52qM


from pulp import *

model = pulp.LpProblem('linear_programming', LpMaximize)

solver = getSolver('PULP_CBC_CMD')

# Definição das variáveis como binárias
x1 = LpVariable('x1', lowBound=0, upBound=1, cat='continuous')
x2 = LpVariable('x2', lowBound=0, upBound=1, cat='continuous')
x3 = LpVariable('x3', lowBound=0, upBound=1, cat='continuous')
x4 = LpVariable('x4', lowBound=0, upBound=1, cat='continuous')

model += 9*x1 + 5*x2 + 6*x3 + 4*x4

# Restrições
model += 6*x1 + 3*x2 + 5*x3 + 2*x4 <= 10
model += x3 + x4 <= 1
model += x3 <= x1
model += x4 <= x2


# restrições da árvore
model += x1 >= 1
model += x2 >= 1
model += x4 <= 0
model += x3 >= 1


# solve
results = model.solve()


# print results
if LpStatus[results] == 'Optimal':
    print('The solution is optimal.')
else:
    print('\033[33mThe solution is not optimal\033[0m')
print(f'Objective value: z* = {value(model.objective)}')
print(f'Solution: '
      f'\nx1* = {value(x1)},'
      f'\n x2* = {value(x2)},'
      f'\n x3 = {value(x3)} ,'
      f'\nx4* = {value(x4)}') 

