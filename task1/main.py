import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import json
import os


def write_to_json_manual(x, y):
    directory = "results"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(f"{directory}/manual.json", "w") as write_file:
        write_file.write('{\n\t"x": [')
        for x_ in x:
            if x_ == x[-1]:
                write_file.write(f'{str(x_)}],')
            else:
                write_file.write(f'{str(x_)}, ')

        write_file.write('\n\t"y": [')
        for y_ in y:
            if y_ == y[-1]:
                write_file.write(f'{str(y_)}]\n')
            else:
                write_file.write(f'{str(y_)}, ')
        write_file.write('}\n')

def write_to_json_lib(x, y):
    data = {}
    data["x"] = list(x)
    data["y"] = list(y)

    directory = "results"
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    with open("results/json_lib.json", "w") as write_file:
        json.dump(data, write_file, indent=4)


def init_params():

    xmin, xmax = -15, 5
    x = np.linspace(xmin, xmax, 50)
    y = np.empty_like(x)

    for i in range(len(x)):
        y[i] = (100 * sqrt(abs(1 - 0.01 * x[i]**2)) + 
                0.01 + abs(x[i] + 10))
        
    return x, y

def main():
    x, y = init_params()
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
    write_to_json_manual(x, y)


main()
