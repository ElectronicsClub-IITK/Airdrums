import numpy as np
from numpy import sqrt
from math import pi
import matplotlib.pyplot as plt

def dft(x):
    N = len(x) #finding out length of x
    n = np.arange(N) #creates sequence of numbers in range N
    k = n.reshape((N, 1)) #this funnctions reeshapes the data without changing the data
    e = np.exp(-2j * np.pi * k * n / N) #fft formmula
    return np.dot(e, x) #multiply every value of the array by the scalar

def generate_noisy_sine_wave(freq, amplitude, noise_level, num_samples):
    t = np.linspace(0, 1, num_samples)
    clean_signal = amplitude * np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(scale=noise_level, size=num_samples)
    noisy_signal = clean_signal + noise
    return noisy_signal

# Parameters
frequency = 5  # Frequency of the sine wave
amplitude = 1  # Amplitude of the sine wave
noise_level = 0.5  # Level of noise to add to the sine wave
num_samples = 1000  # Number of samples in the signal

noisy_signal = generate_noisy_sine_wave(frequency, amplitude, noise_level, num_samples)

# result = cooley_tukey_dft(noisy_signal)
result = dft(noisy_signal)
 
# Compute the magnitude spectrum
magnitude_spectrum = np.abs(result)

# Plot the noisy signal and its magnitude spectrum
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(np.arange(num_samples), noisy_signal)
plt.title('Noisy Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(np.arange(num_samples), magnitude_spectrum)
plt.title('Magnitude Spectrum (DFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
