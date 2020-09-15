import matplotlib.pyplot as plt
import numpy as np

amount_values = 505

x = np.arange(amount_values)
y = x
plt.ylabel('¿Linear stuff?')
plt.xlabel('Some not so random but still very beautiful numbers')
print("Haha, I made some changes.")

plt.plot(x, y)
plt.show()
