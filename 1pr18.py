import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np 

def delta(x):
	if (x>0 or x<0):
		return 0
	else:
		return 1

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

hn = [0, 0.008696617929485395, 0.028592163850781727, 0.06151216564956284]

x = input_signal

for i in range(4, len(x)):
	totx = b[0]*delta(i) + b[1]*delta(i-1) + b[2]*delta(i-2) + b[3]*delta(i-3) + b[4]*delta(i-4)
	toty = a[1]*hn[i-1] + a[2]*hn[i-2] + a[3]*hn[i-3] + a[4]*hn[i-4]
	hn.append((totx-toty)/a[0])

plt.xlim(0, 500)
plt.plot(hn)
plt.show()

sf.write('Sound_with_Reduced_Noise.wav', output_signal, fs)

input_signal, ft = sf.read('Sound_with_Reduced_Noise.wav')
print(ft)
print(a, b)

#plt.plot(output_signal)
#plt.show()