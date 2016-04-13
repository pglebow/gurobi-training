from gurobipy import *

# define index sets and data coefficients
warehouses, capacity = multidict(
  {'A': 6,
   'B': 5,
   'C': 4,
   'D': 6 })

centers, demand = multidict(
  {'X': 3,
   'Y': 3,
   'Z': 8 })

cost = {
  ('A', 'X'): 8, ('A', 'Y'): 6, ('A', 'Z'): 10,
  ('B', 'X'): 3, ('B', 'Y'): 1, ('B', 'Z'): 8,
  ('C', 'X'): 1, ('C', 'Y'): 8, ('C', 'Z'): 5,
  ('D', 'X'): 6, ('D', 'Y'): 2, ('D', 'Z'): 6 }

# create empty model
m = Model()

# add decision variables
# <VARIABLES ADDED HERE>
# Create variables
shipWc = {}
for w in warehouses:
    for c in centers:
        shipWc[w,c] = m.addVar(obj=cost[w,c], name="shipWc_%s_%s" % (w,c))

# process pending changes
m.update()

# set objective function
# <OBJECTIVE SET HERE>
m.setObjective(quicksum(cost[w,c] * shipWc[w,c] for w in warehouses for c in centers))

# add constraints
# <CONSTRAINTS ADDED HERE>
for c in centers:
    m.addConstr(quicksum(shipWc[w,c] for w in warehouses) == demand[c], name=c)

# solve model
m.optimize()

# display solution
if m.SolCount > 0:
  m.printAttr('X')

# export model
m.write('transport.lp')

