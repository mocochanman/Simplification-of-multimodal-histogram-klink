import numpy as np
import optimal_pyramid as defi

#l2二乗距離と近似ヒストグラムの計算
def main_algo(right, x, f, prefix_f, ff):
    wl, wu, = defi.weight(right, x, f, prefix_f)
    p = defi.search_peak(wl, wu, right, ff)
    phi_lx, phi_l, phi_ux, phi_u = defi.phi(right, p, prefix_f)
    phi = defi.approximation(right, phi_lx, phi_l, phi_ux, phi_u, f)
    l2 = defi.l2norm(f, phi)
    return l2, phi, p

def weight(f, min_id):
    w_e = []
    interval = []
    #calcurate average for the interval between min_id
    #
    #
    #
    #

    return w_e