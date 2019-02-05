import pyeeg

fid =open('filteredS.csv','r')
tmp = fid.readlines()
data = [float(k) for k in tmp]
