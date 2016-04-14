from gurobipy import *

m = read('../bell4.mps')
# m.optimize()

# Optimal solution found (tolerance 1.00e-04)
# Best objective 1.854182583800e+07, best bound 1.854002903018e+07, gap 0.0097%

m.Params.MIPGap = 0
m.optimize()

# Optimal solution found (tolerance 0.00e+00)
# Best objective 1.854148419800e+07, best bound 1.854148419800e+07, gap 0.0000%