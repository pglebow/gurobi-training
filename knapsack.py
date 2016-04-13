from gurobipy import *

# define data coefficients
n = 7
p = [6, 5, 8, 9, 6, 7, 3]
w = [2, 3, 6, 7, 5, 9, 4]
c = 9

# create empty model
m = Model()

# add decision variables
# <VARIABLES ADDED HERE>
i = 0
variables = {}
constraints = {}
for v in p:
    variables[i] = m.addVar(vtype=GRB.BINARY, obj=v, name='x'+str(i))
    i = i + 1

# process pending changes
m.update()

# set objective function
# <OBJECTIVE SET HERE>
m.setObjective(quicksum(variables), sense=GRB.MAXIMIZE)

# add constraint
# <CONSTRAINT ADDED HERE>
i = 0
for v in w:
    constraints[i] = m.addConstr(quicksum(variables[i] * w[i]) <= c)
    i = i + 1

# solve model
m.optimize()

# display solution
if m.SolCount > 0:
  m.printAttr('X')

# export model
m.write('knapsack.lp')

