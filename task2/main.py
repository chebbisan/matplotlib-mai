import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import json
import sys

def parse_args():
    params = sys.argv
    xmin = -15
    xmax = 5

    if len(params) < 2:
        print("Invalid params: missing required parameter")
        return {'dir': '',
                'xmin': 0,
                'xmax': 0}
    
    elif len(params) == 3:
        if params[2][:7] == '--xmin=':
            xmin = int(params[2][7:])
        elif params[2][:7] == '--xmax=':
            xmax = int(params[2][7:])

    elif len(params) == 4:
        xmin = int(params[2][7:])
        xmax = int(params[3][7:])

    directory = params[1]
    return {'dir': 'examples/' + directory,
            'xmin': xmin,
            'xmax': xmax}

def main():
        file_params = parse_args()
        directory = file_params['dir']
        if not(directory):
            return
        xmin = file_params['xmin'] if file_params['xmin'] else -15
        xmax = file_params['xmax'] if file_params['xmax'] else 5

        with open(directory, 'r') as read_json:
            data = json.load(read_json)

        fig, ax = plt.subplots()
        ax.plot(data['x'], data['y'])
        plt.xlim(xmin, xmax)

        plt.show()

main()
