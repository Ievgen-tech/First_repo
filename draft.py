# Простий математичний скрипт на Python
# Обчислення квадратної функції та побудова графіка

import numpy as np
import matplotlib.pyplot as plt

# Коефіцієнти функції y = ax^2 + bx + c
a, b, c = 1, -2, -3

# Генеруємо значення x
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

# Виводимо кілька прикладів обчислень
print("Приклад значень:")
for val in [-3, 0, 2]:
    print(f"x = {val}, y = {a*val**2 + b*val + c}")

# Побудова графіка
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f"y = {a}x² + {b}x + {c}", color="blue")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.title("Графік квадратної функції")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()