#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Last Modified time: 2022-05-21
# @Author: Zik.A
# @Email: zik.ai@outlook.com

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.optimize import linprog

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.set_xlabel('Y')
ax.set_ylabel('X')
ax.set_zlabel('Z')
ax.set_title('Linear Prog')

c=[-1,0]
A = [[1,-0.04],[1,0.02],[1,0.04]]
b = [0.086,0.098,0.112]
z_bounds = (None,None)
x_bounds = (0,1)

res = linprog(c, A_ub=A, b_ub=b, bounds=[z_bounds, x_bounds])

print(res)


xx = np.arange(0,1,0.01)
yy = np.arange(0,1,0.01)
X1, Y1 = np.meshgrid(xx, yy)

z = np.empty([100,100],dtype = float)

m,n = 0,0
for i in X1:
    for j in i:
        x,y = xx[m],yy[n]
        if x + y >1:
            z[m,n] = None
        elif 0 <= x <= 0.2:
            z[m,n] = 0.12*x + 0.08*(y - 0.3) + 0.10 * 0.3
        elif 0.2 < x <= 0.7:
            z[m,n] = 0.12 * 0.2 + 0.06*(x - 0.2) + 0.08*(y - 0.3) + 0.10 * 0.3
        elif 0.7 < x <= 1.0:
            z[m,n] = 0.12 * 0.2 + 0.06*(x - 0.2) + 0.10*y
        n+=1
    m+=1
    n=0


z_0 = z.reshape((1,10000))

loc = np.where(z == max(z_0[0]))
print(max(z_0[0]),loc)
ax.plot_surface(X1,Y1,z,cmap='Blues')
plt.show()