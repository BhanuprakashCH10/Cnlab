import numpy as np
import matplotlib.pyplot as plt

data = [1, 0, 1, 0, 1, 1, 0]
samples_per_bit = 200
fc = 20  
fs = samples_per_bit  # Sampling frequency
Ac = 1  # Carrier amplitude
Am = 1  # Message amplitude

nrz_signal = np.repeat([1 if bit == 1 else -1 for bit in data],
                       samples_per_bit)

t = np.arange(len(nrz_signal)) / fs


carrier = Ac * np.sin(2 * np.pi * fc * t)
