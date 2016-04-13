from gurobipy import *

# m = read('../bell4.mps')
# m.optimize()
# m.write('bell4.sol')


m = read('../bell4.mps')
m.read('bell4.sol')
m.optimize()