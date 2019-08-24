import soundfile as sf
from scipy import signal
#https://academo.org/demos/spectrum-analyzer/

input_signal, fs = sf.read('Sound_Noise.wav')
sampl_freq = fs
order = 4
cutoff_freq = 2000.0

x = input_signal
y = [0, 0, 0, 0]
Wn = 1.5*cutoff_freq/sampl_freq

b, a = signal.butter(order, Wn, 'low')

for i in range(4, len(x)):
	totx = b[0]*x[i] + b[1]*x[i-1] + b[2]*x[i-2] + b[3]*x[i-3] + b[4]*x[i-4]
	toty = a[1]*y[i-1] + a[2]*y[i-2] + a[3]*y[i-3] + a[4]*y[i-4]
	y.append((totx-toty)/a[0])
      


output_signal = y

sf.write('Sound_with_Reduced_Noise.wav', output_signal, fs)

input_signal, ft = sf.read('Sound_with_Reduced_Noise.wav')
print(ft)