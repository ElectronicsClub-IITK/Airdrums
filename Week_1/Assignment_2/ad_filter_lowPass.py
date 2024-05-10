import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def generate_noisy_sine_wave(freq, amplitude, noise_level, num_samples):
    t = np.linspace(0, 1, num_samples)
    clean_signal = amplitude * np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(scale=noise_level, size=num_samples)
    noisy_signal = clean_signal + noise
    return noisy_signal


# function for Butterworth high-pass filter
def high_pass_filter(data, cutoff_freq, sampling_freq, order=5):
    nyquist_freq = 0.5 * sampling_freq
    normalized_cutoff_freq = cutoff_freq / nyquist_freq
    b, a = signal.butter(order, normalized_cutoff_freq, btype='low', analog=False)
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data


# Parameters
frequency = 5  # Frequency of the sine wave
amplitude = 1  # Amplitude of the sine wave
noise_level = 0.5  # Level of noise to add to the sine wave
num_samples = 1000  # Number of samples in the sine wave

# generating a noisy signal
signal_with_noise = generate_noisy_sine_wave(frequency,amplitude,noise_level,num_samples)

# setting parameters for the filter
cutoff_freq = 5
sampling_freq = 1000

# filtering the noisy signal
signal_filtered = high_pass_filter(signal_with_noise, cutoff_freq, sampling_freq)

# plotting noisy signal
plt.subplot(2, 1, 1)
plt.plot(np.arange(num_samples), signal_with_noise)
plt.title('noisy signal')
plt.xlabel('time')
plt.ylabel('amplitude')

# plotting filtered signal
plt.subplot(2, 1, 2)
plt.plot(np.arange(num_samples), signal_filtered)
plt.title('filtered signal')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.tight_layout()
plt.show()

