import wget
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from Calculate_EDA import Calculate_EDA, Write_Result

VARIANT = 3

def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True

def init_params():
    if not(exists('task_rcs.csv')):
        wget.download('https://jenyay.net/uploads/Student/Modelling/task_rcs.csv')
        print()

    data = pd.read_csv('task_rcs.csv')

    d = data[' D'][VARIANT - 1]
    fmin = data[' fmin'][VARIANT - 1]
    fmax = data[' fmax'][VARIANT - 1]

    return d, fmin, fmax

def to_csv(freq, wave_len, eda):
    writer = Write_Result(freq, wave_len, eda)
    writer.write('result')

def main():
    diameter, fmin, fmax = init_params()
    frequency = np.linspace(fmin, fmax, 100)
    eda = np.zeros_like(frequency)
    wave_length = np.zeros_like(frequency)
    for i in range(len(frequency)):
        calc = Calculate_EDA(diameter, frequency[i])
        eda[i] = calc.result()
        wave_length[i] = calc.wave_length
        
    fig, ax = plt.subplots()
    ax.plot(frequency, eda)
    plt.ylabel("ЭПР, м^2")
    plt.xlabel("Частота, Гц")
    plt.show()

    to_csv(frequency, wave_length, eda)
  
main()