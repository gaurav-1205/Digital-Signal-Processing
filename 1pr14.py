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

r, p, k = signal.residue(b, a, tol = 0.001, rtype = 'avg')
print(r)
print(p)
print(k)
print(b)
x = range(500)
plt.xlim(0, 500)
hn = [0]

for j in range(500):
	t = 0
	for i in range(4):
		t += r[i]*p[i]**j
	hn.append(t)

plt.plot(hn)
plt.show()
#print(pn)
