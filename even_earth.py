# -*- coding: utf-8 -*-

import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def even_earth():
    r = 1
    para1 = random.uniform(0, 1)
    para2 = random.uniform(0, 1)
    theta = para1 * 2 * math.pi
    #phi = para2 * math.pi
    phi = math.acos(2* para2 - 1)
    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    return x, y, z

if __name__ == "__main__":
    N = 100
    x_sample = []
    y_sample = []
    z_sample = []
    for i in range(N):
        x,y,z = even_earth()
        x_sample.append(x)
        y_sample.append(y)
        z_sample.append(z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_sample, y_sample, z_sample, c='b')
    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()
