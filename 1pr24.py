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

#output_signal = signal.filtfilt(b, a, input_signal)

#plt.plot(output_signal)
#plt.show()

#input_signal, ft = sf.read('Sound_with_Reduced_Noise.wav')
#print(ft)

r, p, k = signal.residue(b, a, tol = 0.001, rtype = 'avg')
#print(r)
#print(p)
#print(k)
#print(b)
x = input_signal
plt.xlim(0, 500)
hn = [0]

for j in range(len(input_signal)):
	t = 0
	for i in range(4):
		t += r[i]*p[i]**j
	hn.append(t)

#print(len(hn))
#print(len(input_signal))
#plt.plot(hn)
#plt.show()
#print(pn)

yn = [0]

for i in range(1000):
	p=0
	print(i, '\b')
	for j in range(i):
		p+=input_signal[j]*hn[i-j]
		
	yn.append(p)

#plt.xlim(0, 1000)
#plt.ylim(-0.4, 0.4)
#plt.plot(yn)
#plt.show()

#for i in (len(yn)):
#	y[i] = float(y[i])


#plt.plot(yn)
#plt.show()
output_signal = yn
#print(type(output_signal[1]))
#sf.write('Sound_with_Reduced_Noise.wav', output_signal, fs)
plt.ylim(-100, 100)
plt.xlim(0, 500)
X = np.fft.fft(x)

plt.plot(np.abs(X))
plt.show()
