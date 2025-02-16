import numpy as np
import matplotlib.pyplot as plt
from DFT import dft

def generate_noisy_sine_wave(freq, amplitude, noise_level, num_samples):
    t = np.linspace(0, 1, num_samples)
    clean_signal = amplitude * np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(scale=noise_level, size=num_samples)
    noisy_signal = clean_signal + noise
    return noisy_signal

def inverse_fourier_transform(signal):
    N = len(signal)
    inverse_signal = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        for k in range(N):
            inverse_signal[n] += signal[k] * np.exp(2j * np.pi * k * n / N)
    inverse_signal /= N
    return inverse_signal

def apply_lowpass_filter(signal):
    fft_signal = dft(signal)
    bandlimit_index = int(len(fft_signal)/35)
    for i in range(bandlimit_index + 1, len(fft_signal) - bandlimit_index ):
            fft_signal[i] = 0
    return inverse_fourier_transform(fft_signal)

# Parameters for the noisy sine wave
frequency = 5  # Frequency of the sine wave
amplitude = 1  # Amplitude of the sine wave
noise_level = 0.5  # Level of noise to add to the sine wave
num_samples = 1000  # Number of samples in the sine wave

# Generate noisy sine wave
noisy_signal = generate_noisy_sine_wave(frequency, amplitude, noise_level, num_samples)

# Parameters for the low-pass filter
cutoff_freq = 5  # Cutoff frequency of the filter in Hz
sampling_freq = 1000  # Sampling frequency of the signal in Hz
order = 5  # Order of the Butterworth filter

# Apply the low-pass filter
filtered_signal = apply_lowpass_filter(noisy_signal)

# Plot the original noisy signal and the filtered signal
plt.figure(figsize=(12, 6))
plt.plot(np.linspace(0, 1, num_samples), noisy_signal, label='Noisy Signal')
plt.plot(np.linspace(0, 1, num_samples), filtered_signal, label='Filtered Signal')
plt.title('Noisy Sine Wave with Low-Pass Filtering')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()