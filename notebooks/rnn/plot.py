import matplotlib.pyplot as plt
import numpy as np

# Define x values
x = np.linspace(-10, 10, 400)

# Define different functions with the same slope but different y-intercepts
y1 = 2*x
y2 = 2*x + 3
y3 = 2*x - 4

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='f(x) = 2x', color='blue')
plt.plot(x, y2, label='f(x) = 2x + 3', color='green')
plt.plot(x, y3, label='f(x) = 2x - 4', color='red')

# Mark the y-intercepts
plt.scatter(0, y1[200], color='blue', s=50)  # y = 0
plt.scatter(0, y2[200], color='green', s=50)  # y = 3
plt.scatter(0, y3[200], color='red', s=50)    # y = -4

# Labels and title
plt.title("Effect of 'b' in f(x) = ax + b")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
