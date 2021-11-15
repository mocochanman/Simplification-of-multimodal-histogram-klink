import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
import sys
import math
#import self definition program
import optimal_pyramid as defi

#l2二乗距離と近似ヒストグラムの計算
def main_algo(right, x, f, prefix_f, ff):
    wl, wu, = defi.weight(right, x, f, prefix_f)
    p = defi.search_peak(wl, wu, right, ff)
    phi_lx, phi_l, phi_ux, phi_u = defi.phi(right, p, prefix_f)
    phi = defi.approximation(right, phi_lx, phi_l, phi_ux, phi_u, f)
    l2 = defi.l2norm(f, phi)
    return l2, phi, p

#データの読み込み
while True:
    name = input("file name >>> ")
    try:
        data = pd.read_csv(str(name)+".csv")
        break
    except FileNotFoundError as e:
        print(e)

f_origin = np.array(list(data['cases']))

#週平均データの計算
weak_f = []
for i in range(6):
    weak_f.append(f_origin[i])

for i in range(6, len(f_origin)):
    ave = f_origin[i]+f_origin[i-1]+f_origin[i-2]+f_origin[i-3]+f_origin[i-4]+f_origin[i-5]+f_origin[i-6]
    weak_f.append(ave//7)

f = np.array(weak_f)
x_f =np.array( [i for i in range(len(f))])

#極小値の集合の抽出
minid = signal.argrelmin(f, order=1)
minimal = minid[0].tolist() #一次元配列化
#先頭にindex 0 と、最後のindexを挿入
minimal.insert(0,0)
minimal.append(len(f)-1)

#リンク数kの入力（整数のみ）
while True:
    try:
        k = int(input("k:peak >>> "))
        break
    except ValueError as e:
        print(e)

#各辺に重みづけを行う.
import make_dag as make
dag = make.weight(f, minimal)

#ここから動的計画法(k,fを入力)
#recurrence formula : dp(j, p) = min(dp(i,p-1) + w(i,j)) p=1,2,...,k
#complexity is O(kn^2)

f_inf = math.inf #initial value of dp table
dp = [[f_inf] * len(minimal) for i in range(k)] #minimum weight of shortest path
dp[0] = dag[0] #init
path = [[[] for i in range(len(minimal))] for j in range(k)] #vertices of path

#if k=0(1), all path is (o, endpoint)
for i in range(len(path[0])):
    path[0][i].append(0)
    if i > 0:
        path[0][i].append(i)

#k=1ならただの単蜂近似
if k == 1:
    sys.exit()

#k>1のときのみk-リンク最短経路を計算する
for k in range(1,k):
    for j in range(len(minimal)):
        for i in range(j):
            w_tmp = dp[k-1][i] + dag[i][j]
            if w_tmp < dp[k][j]:
                dp[k][j] = w_tmp #重みの更新

                path[k][j] = path[k-1][i] + [j]  #更新したらその時のパスを保存しておく

min_weight = dp[-1][-1]
path_tmp = np.array(path[-1][-1])
path_opt = []
for i in range(len(path_tmp)): #dagのノード番号と元のヒストグラムの頂点番号を対応させる
    path_opt.append(minimal[path_tmp[i]])

print(min_weight, path_opt) #check

#plt.bar(x_f, f, width=1.0, edgecolor="black")
plt.plot(x_f, f, color="blue")
plt.scatter(x_f[path_opt], f[path_opt], color='red', zorder=3)
plt.show()