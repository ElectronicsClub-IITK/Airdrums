import numpy as np
import matplotlib.pyplot as plt

def moving_average_filter(signal, window_size):
    filtered_signal = [] # initialize array to store averages
    
    i=0 # counter variable
    while i < len(signal)-window_size+1 : # loop for moving average
        window = signal[i : i + window_size] # creating a window of required size
        window_average = round(sum(window) / window_size , 2) # calculating average of teh window and rounding off
        filtered_signal.append(window_average) # appending the average to the created array
        i+=1
    return filtered_signal

# Parameters
frequency = 5  # Frequency of the sine wave
amplitude = 1  # Amplitude of the sine wave
noise_level = 0.5  # Level of noise to add to the sine wave
num_samples = 1000  # Number of samples in the sine wave

def generate_noisy_sine_wave(frequency, amplitude, noise_level, num_samples):
    t = np.linspace(0, 1, num_samples)
    clean_signal = amplitude * np.sin(2 * np.pi * frequency * t)
    noise = np.random.normal(scale=noise_level, size=num_samples)
    noisy_signal = clean_signal + noise
    return noisy_signal

# generating a noisy signal
signal_with_noise = generate_noisy_sine_wave(frequency,amplitude,noise_level,num_samples)

# setting parameters for the filter
window_size = 3

# filtering the noisy signal
signal_filtered = moving_average_filter(signal_with_noise, window_size)

# plotting noisy signal
plt.subplot(2, 1, 1)
plt.plot(np.arange(num_samples), signal_with_noise)
plt.title('noisy signal')
plt.xlabel('time')
plt.ylabel('amplitude')

num_samples -= (window_size-1) # adjusting for the reduced sample size due to moving average filter

# plotting filtered signal
plt.subplot(2, 1, 2)
plt.plot(np.arange(num_samples), signal_filtered)
plt.title('filtered signal')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.tight_layout()
plt.show()