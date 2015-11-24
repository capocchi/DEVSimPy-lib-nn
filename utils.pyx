
from scipy.special import expit

cdef extern from "math.h":
    float tanh(float theta)
	
cdef dactivation(float y, int function):
    if function == 0:
      return tanh(y)
    elif function == 1:
      return  expit(y)		# sigmoid
    else:
      return 1.0
