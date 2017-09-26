from numba import jit, autojit
@autojit
def calc_sum(a):
    a_cum = 0.
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for n in range(a.shape[2]):
                a_cum = a_cum+a[i,j,n]
    return a_cum

def useless_numba(year):
    #from netCDF4 import Dataset
    f = Dataset('air.sig995.'+year+'.nc')
    a = f.variables['air'][:]
    a_cum = calc_sum(a)
    
    d = np.array(a_cum)
    d.tofile(year+'.bin')
    print(year)
    return d
print(time)