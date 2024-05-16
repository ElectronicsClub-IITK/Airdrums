import matplotlib.pyplot as plt
import numpy as np

#recursive fft function
def recursive_fft(signal):
    
    N = len(signal)
    
    if N == 1: return signal
    else:
        even = recursive_fft(signal[::2])
        odd = recursive_fft(signal[1::2])
        factor = np.exp(-2j*np.pi*np.arange(N)/ N)
        
        result = np.concatenate([even+factor[:int(N/2)]*odd,even+factor[int(N/2):]*odd])
        return result
    
# test input
test = np.array([1,1,1,1,0,0,0,0])

# printing the result of fft
print(recursive_fft(test))

# output
# [ 4.0000000e+00+0.00000000e+00j  1.0000000e+00-2.41421356e+00j
#  -1.2246468e-16-1.22464680e-16j  1.0000000e+00-4.14213562e-01j
#   0.0000000e+00-2.44929360e-16j  1.0000000e+00+4.14213562e-01j
#   1.2246468e-16-1.22464680e-16j  1.0000000e+00+2.41421356e+00j]