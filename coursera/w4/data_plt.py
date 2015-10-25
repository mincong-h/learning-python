# -*- coding: utf-8 -*-
"""
4.2 Python 高级数据处理与可视化

modified for §4.2.3
    add title
    add x, y labels
    update color
    update style

modified for §4.2.4
    add subplots
    more: http://matplotlib.org/examples/pylab_examples/subplot_toolbar.html
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)
y = np.sin(4 * np.pi *x)
np.exp(-5 * x)
plt.subplot(211)
plt.plot(x, y, 'r--')
plt.title('hello python')
plt.xlabel('x')
plt.ylabel('y=sin(x)')
plt.subplot(212)
plt.plot(x, y, 'gD')
plt.title('hello python 2')
plt.xlabel('x')
plt.ylabel('y=sin(x)')
plt.show()
