"""def bin_power(X,Band,Fs):
 C = fft(X)
 C = abs(C)
 Power =zeros(len(Band)-1);
 for Freq_Index in xrange(0,len(Band)-1):
    Freq = float(Band[Freq_Index])										## Xin Liu
    Next_Freq = float(Band[Freq_Index+1])
    Power[Freq_Index] = sum(C[floor(Freq/Fs*len(X)):floor(Next_Freq/Fs*len(X))])

 Power_Ratio = Power/sum(Power)
 return Power_Ratio


def spectral_entropy(X, Band, Fs, Power_Ratio = None):
 if Power_Ratio is None:
    Power_Ratio = bin_power(X, Band, Fs)
 Spectral_Entropy = 0
 for i in xrange(0,len(Power_Ratio)-1):
    Spectral_Entropy += Power_Ratio[i] * log(Power_Ratio[i])
    Spectral_Entropy /= log(len(Power_Ratio))
 return -1 * Spectral_Entropy"""

from pyeeg import*


fid =open('test_control/filteredS.csv','r')
tmp = fid.readlines()
data = [float(k) for k in tmp]

spectral_entropy(data,[0.5,4,7,12,30],128,Power_Ratio = None)
