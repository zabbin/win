#-*- coding: utf-8 -*-

import pylab
import math

# �������� � ����� ������� ����

x1 = range (1, 100)
data1 = [math.exp (-n * n / 1000.0) for n in x1]

# ��������� ���� �� ���  ������ � ��� �������. ����� ����� �������������� � ������ �������
pylab.subplot (2, 2, 1)

# ����� ������
pylab.plot (x1, data1, "r")


# �������� � ������ ������� ����
fracs = [10, 20, 30, 40]

# ��������� ���� �� ���  ������ � ��� �������. ����� ����� �������������� �� ������ �������
pylab.subplot (2, 2, 2)
pylab.pie (fracs)

# �������� �����
x2 = range (0, 720)

data2 = [math.sin (n * math.pi / 180.0) for n in x2]
data3 = [math.sin (n * math.pi / 180.0 + math.pi / 3) for n in x2]

# ��������� ���� �� ��� ������ � ���� �������. ����� ����� �������������� �� ������ �������
pylab.subplot (2, 1, 2)

# ����� ������
pylab.plot (x2, data2)
pylab.plot (x2, data3, "--")

# ������� �������
pylab.legend (["label 1", "label 2"])

# ������� �����
pylab.grid(True)

# ���������� ���
pylab.show()