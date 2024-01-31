import matplotlib

#graph n^2
import matplotlib.pyplot as plt
import numpy as np
def plot_n_sqaured():
    x = np.arange(0, 100, 1)
    y = 2*x**2+3*x+2
    ub = 5*x**2
    lb = (x**2)/2
    plt.plot(x, y)
    plt.plot(x, ub, 'r--')
    plt.plot(x, lb, 'r--')
    #Label the upper and lower bounds
    plt.text(3, 80, '5n^2', fontsize=12, color='red')
    plt.text(6, 11, '(1/2)n^2', fontsize=12, color='red')
    plt.text(4, 40, 'T(n)', fontsize=12, color='blue')
    # Save the plot
    plt.savefig('n^2.png')
    # Axis information
    plt.xlabel('n')
    plt.ylabel('T(n)')
    # Graph title
    plt.title('T(n) = 2n^2+3n+2 with upper and lower bounds')

    # Zoom in the graph
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    # Vertical line at x=1.8
    plt.axvline(x=1.4, color='b', linestyle='--')
    plt.text(0.7, -5, 'x=1.4', fontsize=12, color='blue')

    plt.show()

plot_n_sqaured()