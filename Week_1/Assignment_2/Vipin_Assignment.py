import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 5  # Frequency of the sine wave
amplitude = 1  # Amplitude of the sine wave
noise_level = 0.5  # Level of noise to add to the sine wave
num_samples = 1000  # Number of samples in the sine wave


t = np.linspace(0, 1, num_samples)
clean_signal = amplitude * np.sin(2 * np.pi * frequency * t)
noise = np.random.normal(scale=noise_level, size=num_samples)
signal = clean_signal + noise



def DFT(signal):
    """
    Compute the Discrete Fourier Transform of the given signal.
    
    Args:
    - signal (array_like): Input signal
    
    Returns:
    - array_like: The discrete Fourier Transform of the input signal
    """
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    exp_term = np.exp(-2j * np.pi * k * n / N)
    return np.dot(exp_term, signal)


def FFT(signal):
    """
    Compute the Fast Fourier Transform of the given signal.
    
    Args:
    - signal (array_like): Input signal
    
    Returns:
    - array_like: The Fast Fourier Transform of the input signal
    """
    signal = np.asarray(signal, dtype=float)
    N = len(signal)
    if N <= 1:
        return signal
    else:
        # Pad the signal with zeros to the next power of 2
        next_power_of_2 = int(2**np.ceil(np.log2(N)))
        padded_signal = np.pad(signal, (0, next_power_of_2 - N), mode='constant')
        even = FFT(padded_signal[::2])
        odd = FFT(padded_signal[1::2])
        t = np.exp(-2j * np.pi * np.arange(next_power_of_2) / next_power_of_2)
        return np.concatenate([even + t[:next_power_of_2//2] * odd, even + t[next_power_of_2//2:] * odd])


    
def moving_average_filter(signal, window_size):
    """
    Apply a simple moving average filter to the input signal.
    
    Args:
    - signal (array_like): Input signal
    - window_size (int): Size of the moving average window
    
    Returns:
    - array_like: The filtered signal
    """
    return np.convolve(signal, np.ones(window_size)/window_size, mode='valid')

# Compute FFT and DFT of the signal
fft_signal = FFT(signal)
dft_signal = DFT(signal)

# Apply a moving average filter
filtered_signal = moving_average_filter(signal, 10)

# Plot the signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 2)
plt.plot(np.abs(fft_signal))
plt.title('FFT of Signal')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.subplot(2, 2, 3)
plt.plot(np.abs(dft_signal))
plt.title('DFT of Signal')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.subplot(2, 2, 4)
plt.plot(t[:-9], filtered_signal)
plt.title('Filtered Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
