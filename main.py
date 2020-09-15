import matplotlib.pyplot as plt
import numpy as np

amount_values = 70
x = np.arange(amount_values)
y = np.random.normal(size=(amount_values))
plt.ylabel('Some beautiful random numbers')
plt.xlabel('Some not so random but still very beautiful numbers')
print("Haha, I made some changes.")

plt.plot(x, y)
plt.show()