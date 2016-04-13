import gurobipy
model = gurobipy.read('/Library/gurobi651/mac64/examples/data//afiro.mps')
model.optimize()
model.printAttr('X')