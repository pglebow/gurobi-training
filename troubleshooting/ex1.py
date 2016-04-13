from gurobipy import *

m = read('../bell4.mps')
m.optimize()
m.reset()
m.Params.threads=1
m.optimize