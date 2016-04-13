# import gurobipy module
from gurobipy import *

fileName = 'PhilModel.mps'

# create empty model
m = Model()

# change model name attribute
m.ModelName = 'Phil Model'

# process the pending change
m.update()

# export model to file
m.write(fileName)

# print to console
print 'This program creates an empty model named:', m.Modelname
print 'Model exported to file named: ', fileName

