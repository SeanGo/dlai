# GRADED FUNCTION: basic_sigmoid

import math
import numpy as np

def sigmoid(x):
    """
    Compute sigmoid of x.

    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ###
    s = 1 / ( 1 + np.exp(-x))
    ### END CODE HERE ###
    
    return s


print sigmoid(3)
x = np.array([1, 2, 3])
print sigmoid(x)

