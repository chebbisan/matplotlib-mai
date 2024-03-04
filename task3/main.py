import matplotlib.pyplot as plt
import numpy as np

D = 2

def ackley_function(x1, x2):
    term1 = -0.02 * np.sqrt((x1**2 + x2**2) / D)
    term2 = (np.cos(2*np.pi*x1) + np.cos(2*np.pi*x2)) / D

    return -20 * np.exp(term1) - np.exp(term2)

def main():
    fig = plt.figure(figsize=(8, 8))

    x1 = np.linspace(-5, 5, 100)
    x2 = np.linspace(-5, 5, 100)

    ax1 = fig.add_subplot(221, projection='3d')
    x, y = np.meshgrid(x1, x2)
    z = ackley_function(x, y)
    ax1.plot_surface(x, y, z, cmap='Spectral')
    ax1.set_xlabel('x1')
    ax1.set_ylabel('x2')
    ax1.set_zlabel('y=f(x1, x2)')


    ax2 = fig.add_subplot(222, projection='3d')
    ax2.plot_surface(x, y, z, cmap='Spectral')
    ax2.view_init(elev=90, azim=0)
    ax2.set_xlabel('x1')
    ax2.set_ylabel('x2')
    ax2.set_zlabel('y=f(x1, x2)')
    ax2.axes.zaxis.set_ticklabels([])
    


    ax3 = fig.add_subplot(223)
    x = np.linspace(-5, 5, 100)
    y = ackley_function(x, 0)
    ax3.plot(x, y, color='wheat')
    ax3.set_xlabel('x1')
    ax3.set_ylabel('y=f(x1, 0)')
    


    ax4 = fig.add_subplot(224)
    x = np.linspace(-5, 5, 100)
    y = ackley_function(0, x)
    ax4.plot(x, y, color='peru')
    ax4.set_xlabel('x2')
    ax4.set_ylabel('y=f(0, x2)',labelpad=-265)
    ackley_0_0 = ackley_function(0, 0)
    plt.text(-6, -19, f'Координаты тестовой точки: (0; 0)\nf(0, 0) = {ackley_0_0}')
    

    plt.show()

main()