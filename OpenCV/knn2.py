import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
response = np.random.randint(0, 2, (25, 1)).astype(np.float32)

red = trainData[response.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
blue = trainData[response.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

for i in range(10):
    print(red[i], blue[i])
    print(red[i][0])

plt.show()