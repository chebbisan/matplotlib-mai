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


    ax2 = fig.add_subplot(222, projection='3d')
    ax2.plot_surface(x, y, z, cmap='Spectral')
    ax2.view_init(elev=90, azim=0)


    ax3 = fig.add_subplot(223)
    x = np.linspace(-5, 5, 100)
    y = ackley_function(x, 0)
    ax3.plot(x, y, color='wheat')


    ax4 = fig.add_subplot(224)
    x = np.linspace(-5, 5, 100)
    y = ackley_function(0, x)
    ax4.plot(x, y, color='peru')

    plt.show()

main()