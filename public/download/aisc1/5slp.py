
import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([0,0,0,1])
W = np.array([0.0, 0.0])
b = -0.5
lr = 0.1

def activation(x):
    return 1 if x >= 0 else 0

for epoch in range(10):
    for i in range(len(X)):
        output = activation(np.dot(X[i], W) + b)
        error = Y[i] - output
        W += lr * error * X[i]
        b += lr * error

print("Final Weights:", W)
print("Final Bias:", b)
print("\nFinal Output:")

for x in X:
    output = activation(np.dot(x, W) + b)
    print("Input =", x, "Output =", output)
