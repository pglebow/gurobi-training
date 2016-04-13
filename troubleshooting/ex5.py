from gurobipy import *

m = read('pds-40.mps')
m.tune()