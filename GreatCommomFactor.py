# great common factor
# 时间复杂度 >log(N),真实值2log(N)

def Gcf(M,N):

    if N>M: # switch
        temp = M
        M = N
        N = temp
    while( N > 0):
        temp = M % N
        M = N
        N = temp
    return M

print(Gcf(50,15))

