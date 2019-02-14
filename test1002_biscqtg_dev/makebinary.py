import os
import numpy as np
    
files = [f for f in os.listdir('.') if 'biscayne.rch.sp' in f and 'bin.dat' not in f]
files = ['biscayne.rch.zero.dat'] + files 

edtype = np.dtype([('node', np.int32), ('rate', np.float64)]) 
for f in files:
    d = np.genfromtxt(f, dtype=edtype, skip_header=0)
    os.remove(f)
    f = os.path.join('data', f.replace('.dat', '.bin.dat'))
    d.tofile(f)     
files = [f for f in os.listdir('.') if 'biscayne.evt.sp' in f and 'bin.dat' not in f]

edtype = np.dtype([('node', np.int32), ('surface', np.float64),
                   ('rate', np.float64), ('depth', np.float64)]) 
for f in files:
    d = np.genfromtxt(f, dtype=edtype, skip_header=1)
    os.remove(f)
    f = os.path.join('data', f.replace('.dat', '.bin.dat'))
    d.tofile(f) 
