import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np 
#https://academo.org/demos/spectrum-analyzer/

input_signal, fs = sf.read('Sound_Noise.wav')
sampl_freq=fs
#print(input_signal)

order = 4

print(fs)

cutoff_freq = 4000.0

Wn = 1.5*cutoff_freq/sampl_freq

b, a = signal.butter(order, Wn, 'low')

output_signal = signal.filtfilt(b, a, input_signal)

sf.write('Sound_with_Reduced_Noise.wav', output_signal, fs)

input_signal, ft = sf.read('Sound_with_Reduced_Noise.wav')
print(ft)
print(a, b)
plt.xlim(0, 1000)
plt.ylim(-0.4, 0.4)
plt.plot(output_signal)
plt.show()