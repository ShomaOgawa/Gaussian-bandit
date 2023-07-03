#input
import numpy as np
import matplotlib.pyplot as plt

def N(x,mu,sigma):
    return (1/np.sqrt(2*np.pi*sigma))*np.exp(-(x-mu)**2 / (2*sigma**2))

fig = plt.figure()

A = fig.add_subplot(111)
#A.grid(color="k",linestyle="dotted")
#A.set_title("normal distribution", fontsize = 16)
A.set_xlabel("reward", fontsize = 14)
A.set_ylabel("probability density", fontsize = 14)

A.set_xlim([-4, 4])
A.set_ylim([0, 0.45])

x = np.arange(-10, 10, 0.01)

y1 = N(x, 1, 1.0)
y2 = N(x, 0.8, 1.0)
y3 = N(x, 0.5, 1.0)
y4 = N(x, 0, 1.0)

A.plot(x, y1, color="red", label="μ=1.0, σ=1.0")
A.plot(x, y2, color="orange", label="μ=0.8, σ=1.0")
A.plot(x, y3, color="green", label="μ=0.5, σ=1.0")
A.plot(x, y4, color="blue", label="μ=0.0, σ=1.0")
A.grid(True)

A.legend()
plt.show()