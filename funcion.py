
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,4*np.pi)
y=np.sin(x)
plt.plot(x,y)
plt.title("gráfica del sin")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.savefig("grafica.png")