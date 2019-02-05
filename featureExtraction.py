import pyeeg

fid =open('test_control/filteredS.csv','r')
tmp = fid.readlines()
data = [float(k) for k in tmp]
