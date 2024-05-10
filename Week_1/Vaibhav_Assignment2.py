import numpy as np
import matplotlib.pyplot as plt

def generate_noisy_sine_wave(freq, amplitude, noise_level, num_samples):
    t = np.linspace(0, 1, num_samples)
    clean_signal = amplitude * np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(scale=noise_level, size=num_samples)
    noisy_signal = clean_signal + noise
    return noisy_signal

def fft_recursive(x):
    #Compute the Fast Fourier Transform (FFT) using a recursive algorithm.
    N = len(x)
    if N <= 1:
        return x
    else:
        even = fft_recursive(x[0::2])
        odd = fft_recursive(x[1::2])
        T = [0] * N
        for k in range(N // 2):
            T[k] = even[k] + np.exp(-2j * np.pi * k / N) * odd[k]
            T[k + N // 2] = even[k] - np.exp(-2j * np.pi * k / N) * odd[k]
        return T
    
def goertzel_dft(x, k):
    #Compute the DFT at a specific target frequency using the Goertzel algorithm.
    N = len(x)
    wk = np.exp(-2j * np.pi * k / N)
    s = 0
    y = 0
    for n in range(N):
        s = x[n] + wk * s
        y = wk * y + s
    return y

def moving_average_filter(x, n):
    """
    Apply a moving average filter of length n to the signal x.

    Parameters:
    x (numpy.ndarray): The input signal.
    n (int): The length of the moving average filter.

    Returns:
    numpy.ndarray: The filtered signal.
    """
    y = np.convolve(x, np.ones(n)/n, mode='same')
    return y

freq = 5  # Frequency of the sine wave
amplitude = 1  # Amplitude of the sine wave
noise_level = 0.5  # Level of noise to add to the sine wave
num_samples = 1000  # Number of samples in the sine wave
t = np.linspace(0, 1, num_samples)

signal = generate_noisy_sine_wave(freq, amplitude, noise_level, num_samples)

fft_result = fft_recursive(signal)
print(fft_result)
print("\n")
#fft_result: numpy array containing the FFT result
dft_result = goertzel_dft(signal , freq-1)
print(dft_result)
#dft_result: DFT magnitude at the target frequency

# Apply the moving average filter to the noisy signal
signal_filtered = moving_average_filter(signal, 101)

# Plot the unfiltered and filtered signals
plt.plot(t, signal, label='Unfiltered')
plt.plot(t, signal_filtered, label='Filtered')
plt.legend()
plt.show()




