import numpy as np
import matplotlib.pyplot as plt

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
num_samples = 1000  # Number of samples in the sine wave

# generating a noisy signal
signal_with_noise = generate_noisy_sine_wave(frequency,amplitude,noise_level,num_samples)

# discrete fourier transform
dft = np.fft.fft(signal_with_noise)

# using absolute function for magnitudes
magnitude = np.abs(dft)

# plotting noisy signal
plt.subplot(2, 1, 1)
plt.plot(np.arange(num_samples), signal_with_noise)
plt.title('noisy signal')
plt.xlabel('time')
plt.ylabel('amplitude')

# plotting magnitude spectrum
plt.subplot(2, 1, 2)
plt.plot(np.arange(num_samples), magnitude)
plt.title('Magnitude Spectrum (DFT)')
plt.xlabel('frequency (Hz)')
plt.ylabel('magnitude')

plt.tight_layout()
plt.show()