import numpy as np

def cooley_tukey_dft(x):
    N = len(x)
    if N == 1:
        return x
    else:
        even = cooley_tukey_dft(x[::2])
        odd = cooley_tukey_dft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([even + factor[:N//2] * odd, even + factor[N//2:] * odd])

# Input sequence
x = np.array([1, 1, 1, 1, 0, 0, 0, 0])

# Compute DFT using Cooley-Tukey algorithm
dft_result = cooley_tukey_dft(x)

print("DFT Result:", dft_result)