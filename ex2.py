from gurobipy import *
model = read('/Library/gurobi651/mac64/examples/data/coins.lp')
model.printStats()
model.optimize()

for v in model.getVars():
    if v.x != 0:
        print v.VarName, v.x