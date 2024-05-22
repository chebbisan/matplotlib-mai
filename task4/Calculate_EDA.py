import scipy.constants as constants
import scipy.special as special
import pandas as pd
import numpy as np

class Calculate_EDA:
    def __init__(self, diameter, frequency):
        self.radius = diameter / 2
        self.wave_length = 0
        self.k = 0
        self.update(frequency)

    def update(self, frequency):
        self.wave_length = np.longdouble(constants.speed_of_light / frequency)
        self.k = np.longdouble(2 * constants.pi / self.wave_length)

    def a_n(self, n):
        numerator = np.longdouble(special.spherical_jn(n, self.k * self.radius))
        divider = self.h_n(n, self.k * self.radius)
        return np.divide(numerator, divider)

    def b_n(self, n):
        numerator = self.k * self.radius * np.longdouble(special.spherical_jn(n-1, self.k * self.radius)) - n * np.longdouble(special.spherical_jn(n, self.k * self.radius))
        divider = self.k * self.radius * self.h_n(n-1, self.k * self.radius) - n * self.h_n(n, self.k * self.radius)
        return np.divide(numerator, divider)

    def h_n(self, n, arg):
        return np.clongdouble(special.spherical_jn(n, arg) + 1j*special.spherical_yn(n, arg))
    
    def result(self):
        coef = self.wave_length**2 / constants.pi
        series_sum = 0
        for n in range(1, 51):
            series_sum += (-1)**n * (n + 0.5) * (self.b_n(n) - self.a_n(n))
        result = coef * np.abs(series_sum)**2
        return result
    


class Write_Result:
    def __init__(self, frequency, wave_length, eda):
        self.len = [x for x in range(1, len(frequency)+1)]
        self.frequency = frequency
        self.wave_length = wave_length
        self.eda = eda

    def write(self, name):
        df = pd.DataFrame({'#': self.len,
                           'freq': self.frequency,
                           'wave_len': self.wave_length,
                           'eda': self.eda})
        df.to_csv(f'{name}.csv', index=False)
