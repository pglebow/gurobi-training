from gurobipy import *

m = read('/Users/pglebow/85_1PAMM_Model.lp')
m.Params.MIPGap = 0
m.optimize()
