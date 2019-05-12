import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return (1.0 / (1 + np.exp(-x)))

def unit_step(x):
    return np.array(x > 0 , dtype=np.int)

def Relu(x):
    return np.maximum(x,0)

x = np.arange(-1.0, 1.0, 0.1)
y1 = sigmoid(x)
y2 = unit_step(x)
y3 = Relu(x)
plt.subplot(221)
plt.plot(x,y1)
plt.subplot(222)
plt.plot(x,y2)
plt.subplot(223)
plt.plot(x,y3)

plt.show()

