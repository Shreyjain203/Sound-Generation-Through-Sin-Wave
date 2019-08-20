from numpy import linspace,sin,pi,int16


import winsound



# tone synthesis
def note(freq, len, amp=1, rate=44100):
    t = linspace(0,len,len*rate)
    data = sin(2*pi*freq*t)*amp
    return data.astype(int16) # two byte integers


from scipy.io.wavfile import write
from pylab import plot,show,axis

# A tone, 1 seconds, 44100 samples per second

freq = 622
amp = 10000
length = 1

tone = note(freq,len = length,amp=amp)
winsound.PlaySound(tone,winsound.SND_ASYNC)
#write(44100,tone)

# writing the sound to a file

plot(linspace(0,2,2*44100),tone)
axis([0,0.4,15000,-15000])
show()
