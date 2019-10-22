
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,4*np.pi)
y=np.cos(x)
plt.plot(x,y)
plt.title("gráfica del cos")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.savefig("grafica.png")