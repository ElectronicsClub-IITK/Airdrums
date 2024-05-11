import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

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

# utility function to extend an array until its length is a power of two
def extend_array_to_lowest_power_of_two(array):
    size_of_array = len(array)  # size of array
    required_size = 1           # variable to count the required size

    while(required_size < size_of_array):   # loop that increases the required size until it exceeds the array
        required_size *= 2

    for i in range(required_size - size_of_array):  # the new array is filled with zeroes
        array.append(0)


# utility function to rearrange the elements of an array into first the even terms, and then the odd terms
def rearrange_into_even_and_odd(array):
    half_len = len(array)/2     # length of half the array
    i = 0                       # counter variable

    even_array = []             # initializing the array of even elements
    odd_array = []              # initializing the array of odd elements

    while (i < half_len):       # alternately dropping the elements into even/odd arrays
        even_array.append(array[i*2])
        odd_array.append(array[i*2 + 1])
        i += 1

    return even_array, odd_array

# main recursive algorithm that assumes array already has a size of power of 2
def ct_fft(array):

    if len(array) == 2: # base case
        a, b = array
        return [a+b, a-b]   # result of dft matrix multiplication when n = 2

    else:   # recursive case
        
        even_array, odd_array = rearrange_into_even_and_odd(array)
        
        # recursive call to calculate ffts of the two sub arrays
        array = ct_fft(even_array) + ct_fft(odd_array)

        # computing lengths of array
        full = len(array)
        half = int(full/2)

        # recombining the ffts of the sub arrays
        for k in range(half): # premultiplication of the recursively computed matrices with [I, -D, I, -D]
            p = array[k]
            q = array[k + half] * cmath.exp(-2j * math.pi * k / full) # exp(-2pi i k / N)
            array[k] = p + q
            array[k + half] = p - q

        return array


if __name__ == "__main__":

    # initalizing the time_axis, threshold and noisy signal
    t = np.linspace(0, 1, num_samples)
    threshold = 100
    noisy_signal = generate_noisy_sine_wave(frequency, amplitude, noise_level, num_samples)

    # initializing plot
    plt.figure(figsize=(10, 8))
    plt.suptitle("Implementing FFT & Noise Filter")

    # plotting the noisy sine wave
    plt.subplot(2, 2, 1)
    plt.plot(t, noisy_signal, linewidth=0.5, label='Noisy Sine Wave')
    plt.xlabel('time', fontsize=15)
    plt.ylabel('amplitude', fontsize=15)

    # converting the noisy signal into a regular array
    nsy_arr = list(noisy_signal)
    extend_array_to_lowest_power_of_two(nsy_arr)
    tr_arr = ct_fft(nsy_arr)

    # computing the magnitudes of the frequencies 
    mgn_arr = []
    for i in range(num_samples):
        mgn_arr.append(abs(tr_arr[i]))

    # plotting the fourier transform
    plt.subplot(2, 2, 2)
    plt.plot(t, mgn_arr, linewidth=0.5, label='Fourier Transform')
    plt.xlabel('frequency', fontsize=15)
    plt.ylabel('magnitude', fontsize=15)

    # cleaning out the fourier transform
    clean_arr = []
    for i in range(num_samples):
        if mgn_arr[i] > threshold:
            clean_arr.append(1)     # values over the threshold are kept
        else:
            clean_arr.append(0)     # values below the threshold are killed

    # plotting the cleaned out fourier transform
    plt.subplot(2, 2, 3)
    plt.plot(t, clean_arr, linewidth=0.5, label='Cleaned out Fourier Transform')
    plt.xlabel('frequency', fontsize=15)
    plt.ylabel('magnitude', fontsize=15)

    # reconstucting the clean signal from the fourier transform
    clean_signal = 0
    for i in range(num_samples):
         if clean_arr[i] != 0:
            clean_signal += clean_arr[i] * np.sin(2 * np.pi * i * t) # each frequency of the cleaned signal, is multiplied by its magnitude and added to the final signal

    # plotting the final clean signal
    plt.subplot(2, 2, 4)
    plt.plot(t, clean_signal, linewidth=0.5, label='Reconstructed Clean Signal')
    plt.xlabel('time', fontsize=15)
    plt.ylabel('amplitude', fontsize=15)

    # showing the plot
    plt.tight_layout()
    plt.show()



