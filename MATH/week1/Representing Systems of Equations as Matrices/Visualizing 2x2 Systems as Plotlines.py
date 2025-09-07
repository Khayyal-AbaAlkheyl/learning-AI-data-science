import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import reshape

A=np.array([[-1,3],[3,2]],dtype=float)
print(A)

b = np.array([7,1],dtype=float)
print(b)
reshapedB=b.reshape((2,1))

A_system=np.hstack((A,reshapedB))
print(A_system)


print('-------------------------------')
print(A_system[1])

def plot_lines(A, b):
    x_vals = np.linspace(-10, 10, 200)  # توليد قيم x من -10 إلى 10

    plt.figure(figsize=(8, 6))

    # رسم كل معادلة (خط) في النظام
    for i in range(A.shape[0]):
        a1, a2 = A[i]
        if a2 != 0:
            y_vals = (b[i] - a1 * x_vals) / a2
            plt.plot(x_vals, y_vals, label=f"Eq {i+1}: {a1}x + {a2}y = {b[i]}")
        else:
            # إذا a2 = 0 → خط رأسي
            x = b[i] / a1
            plt.axvline(x=x, label=f"Eq {i+1}: x = {x}")

    # تنسيق الرسم
    plt.axhline(0, color='black', linewidth=0.5)  # المحور x
    plt.axvline(0, color='black', linewidth=0.5)  # المحور y
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphical Representation of the System')
    plt.legend()
    plt.show()

plot_lines(A,b)
