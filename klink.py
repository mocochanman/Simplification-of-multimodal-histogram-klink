import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt
import pandas as pd
import math
import optimal_pyramid as defi

#approcimating and calcuration of error method
def main_algo(right, x, f, prefix_f, ff):
    wl, wu, = defi.weight(right, x, f, prefix_f)
    p = defi.search_peak(wl, wu, right, ff)
    phi_lx, phi_l, phi_ux, phi_u = defi.phi(right, p, prefix_f)
    phi = defi.approximation(right, phi_lx, phi_l, phi_ux, phi_u, f)
    l2 = defi.l2norm(f, phi)
    return l2, phi, p

#import data
while True:
    name = input("file name >>>")
    try:
        data = pd.read_csv(str(name)+".cav")
        break
    except FileNotFoundError as e:
        print(e)
f = np.array(list(data['cases']))
x = np.array([i for i in range(len(f))])

#calcurate weak average data
weak_f = []
for i in range(6):
    weak_f.append(f[i])
for i in range(6, len(f)):
    ave = f[i]+f[i-1]+f[i-2]+f[i-3]+f[i-4]+f[i-5]+f[i-6]
    weak_f.append(ave//7)

weak_f = np.array(weak_f)

#get set of minimal
min_tmp = sig.argrelmin(f, order=1)
min_id = min_tmp[0].tolist() #1 dim list
#insert 0 at first and last index
min_id.insert(0, 0)
min_id.append(len(f)-1)

#input k which is num of link
while True:
    try:
        k = int(input("k:peak >>> "))
        break
    except ValueError as e:
        print(e)

#init weight of edge
