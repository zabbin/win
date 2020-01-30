import numpy as np
import random
import matplotlib.pyplot as plt
N = 1000

# print("���� - ��������� 1 \n")
arr1 = np.array([random.randint(-100,100) for i in range(N)])

# print("���� - ��������� 2 \n")
arr2 = np.array([random.randint(-100,100) for i in range(N)])

# ������
dt = 1
t = np.arange(0, N, dt)
fig, ax = plt.subplots(1,1, figsize=(20, 10))
ax.plot(t, arr1, t, arr2)
ax.set_xlabel('t')
ax.set_ylabel('arr1 and arr2')
ax.grid(True)
plt.show()


# arr1 - �������
sumx1 = 0
k = 0
for k in range(N - 1):
    sumx1 = sumx1 + arr1[k]
x1 = 1/N * sumx1
print('arr1 -  �������: ',x1)

# arr1 - ���������
sumd1 = 0
k = 0
for k in range(N - 1):
    sumd1 = (arr1[k] - x1) * (arr1[k] - x1)
D1 = 1/N * sumd1
print('arr1 -  ���������: ',D1)
print('\n')

# arr2 - �������
sumx2 = 0
k = 0
for k in range(N - 1):
    sumx2 = sumx2 + arr2[k]
x2 = 1/N * sumx2
print('arr2 -  �������: ',x2)

# arr2 - ���������
sumd2 = 0
k = 0
for k in range(N - 1):
    sumd2 = (arr2[k] - x2) * (arr2[k] - x2)
D2 = 1/N * sumd2
print('arr2 -  ���������: ',D2)