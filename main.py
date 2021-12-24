import numpy as np
from matplotlib import pyplot as plt

Vref = 999

k = 1.1547

a = 2

encoderTicksPerHalfRev = 48

dots = encoderTicksPerHalfRev*a

x = np.linspace(0, a*np.pi, dots)

yA = np.sin(x) * Vref
yB = np.sin(x + 2*np.pi/3) * Vref
yC = np.sin(x + 4*np.pi/3) * Vref

yA1 = np.round(yA * k, 3)
yB1 = np.round(yB * k, 3)
yC1 = np.round(yC * k, 3)


yTH = 0.2*Vref*np.sin(3*x)

yA2 = np.round(yA1 + yTH)
yB2 = np.round(yB1 + yTH)
yC2 = np.round(yC1 + yTH)

plt.plot(x, [Vref]*dots, x, [-Vref]*dots, x, yA2, x, yB2, x, yC2)
plt.show()

print("{")
for i, j, k in zip(yA2, yB2, yC2):
    print("{" + f"{int(i)}, {int(j)}, {int(k)}" + "},")
print("}")

print(len(yA2))