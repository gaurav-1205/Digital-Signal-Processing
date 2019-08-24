import soundfile as sf
from scipy import signal
from sympy import *
import sys
sys.displayhook = pprint
z = symbols('z')
#https://academo.org/demos/spectrum-analyzer/

input_signal, fs = sf.read('Sound_Noise.wav')
sampl_freq=fs
#print(input_signal)

order = 4

#print(fs)

cutoff_freq = 4000.0

Wn = 1.5*cutoff_freq/sampl_freq

b, a = signal.butter(order, Wn, 'low')

output_signal = signal.filtfilt(b, a, input_signal)

sf.write('Sound_with_Reduced_Noise.wav', output_signal, fs)

input_signal, ft = sf.read('Sound_with_Reduced_Noise.wav')
#print(ft)
#print(a, b)

sum1 = 0
sum2 = 0
for i in range(5):
	sum1 = sum1 + b[i]*z**(4-i)
	sum2 = sum2 + a[i]*z**(4-i)

q, r = div(sum1, sum2, z)

print(q)
print(r)