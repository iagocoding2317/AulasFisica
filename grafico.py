import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-10,10,100)
y = np.cos(x)

plt.plot(x,y,label='f(x)=x²')
plt.title('Gráfico da função quadrática')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.legend()
plt.show()
