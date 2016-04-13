from gurobipy import *

m = Model('basic')

modelFileName='basic.lp'
solFileName='basic.sol'

x = m.addVar(name='x')
y = m.addVar(name='y')
z = m.addVar(name='z')

m.update()

m.addConstr(x + 2 * y + z <= 4, 'c0')
m.addConstr(x - y == 0, 'c1')
m.addConstr(x >= 0, 'c2')
m.addConstr(y >= 0, 'c3')
m.addConstr(z >= 0, 'c4')

m.setObjective(2 * x + y + z, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)

m.write(modelFileName)
m.write(solFileName)