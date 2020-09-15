import matplotlib.pyplot as plt
import numpy as np

amount_values = 15
x = np.arange(amount_values)
y = x
plt.ylabel('¿Linear stuff?')
plt.xlabel('Some not so random but still very beautiful numbers')

plt.plot(x, y)
plt.show()