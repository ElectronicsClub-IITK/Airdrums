import numpy as np
import math
from matplotlib import pyplot as plt
OP=0

def fft(x):
	global OP

	N = len(x)

	if N == 1:
		return [x[0]]

	X = [0] * N

	even = fft(x[:N:2])
	odd = fft(x[1:N:2])

	for k in range(N//2):
		w = math.e**(-2j*math.pi * k/N)
		X[k] = even[k] + w * odd[k]
		X[k + N//2] = even[k] - w * odd[k]
		OP += 2

	return X

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

# Generate the noisy sine wave
noisy_signal = generate_noisy_sine_wave(frequency, amplitude, noise_level, num_samples)

# Perform FFT using the implemented function
fft_result = fft(noisy_signal)

# Print the FFT result
print("FFT result:", fft_result)
plt.subplot(2, 1, 2)
plt.plot(np.arange(num_samples), fft_result)
plt.title('FFT Result (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
