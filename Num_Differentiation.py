import numpy as np
# Example function
def f(x):
    return x**2 + 3*x+2
# Derivative using Forward Difference
def forward_difference(f,x,h = 1e-5):
    return ( f(x+h) - f(x) ) / h


# Derivative using Central Difference
def central_difference(f,x,h = 1e-5):
    return ( f(x+h) - f(x-h) ) / (2*h)
# Derivative using Backward Difference
def backward_difference(f,x,h = 1e-5):
    return ( f(x) - f(x -h) ) / h
# Test point
x = 2
# Calculate the derivative at x using both methods
fd_result = forward_difference(f,x)
cd_result = central_difference(f,x)
bd_result = backward_difference(f,x)
print (" Forward Difference result : ", fd_result )
print (" Central Difference result : ", cd_result )
print (" Backward Difference result : ", bd_result )