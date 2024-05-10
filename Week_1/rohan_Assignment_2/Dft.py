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
num_samples = 1000  # Number of samples in the sine wave

# Generate noisy sine wave
noisy_signal = generate_noisy_sine_wave(frequency, amplitude, noise_level, num_samples)

# Compute the DFT using FFT
dft = np.fft.fft(noisy_signal)

# Compute the magnitude spectrum
magnitude_spectrum = np.abs(dft)

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