import math
import matplotlib.pyplot as plt
import numpy as np

#This is for ATLAS style plots
#If you want to speed up this part, consider turning Latex off in the parameters
import homogenize_plot as hp
hp.set_params()

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a


x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)
plt.plot(x,sig, linewidth=2.5)
plt.margins(x=0.01)
plt.margins(y=0.01)
plt.xlabel("Input")
plt.ylabel("Output")
plt.vlines(0,0,1.,'k')
plt.savefig('sigmoid.png')