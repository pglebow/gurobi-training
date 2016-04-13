from gurobipy import *

# Compute an IIS

m = read('bell4inf.mps')
m.optimize()
m.computeIIS()
m.write('bell4.ilp')