import numpy as np
import matplotlib.pyplot as plt

# discrete fourier transform function
def discrete_fourier_transform(signal):
    length = len(signal) # length of input signal
    n = np.arange(length) # create index array of size equal to length of signal
    k = n.reshape((length, 1)) # create index array
    M = np.exp(-2j * np.pi * k * n / length) # computing the DFT matrix
    return np.dot(M, signal) # return the matrix multiplication of DFT matrix and input signal


# test input
test = np.array([1,1,1,1,0,0,0,0])

# printing the result of dft
print(discrete_fourier_transform(test))

# output
# [ 4.0000000e+00+0.00000000e+00j  1.0000000e+00-2.41421356e+00j
#  -1.2246468e-16-1.22464680e-16j  1.0000000e+00-4.14213562e-01j
#   0.0000000e+00-2.44929360e-16j  1.0000000e+00+4.14213562e-01j
#   3.6739404e-16-3.67394040e-16j  1.0000000e+00+2.41421356e+00j]