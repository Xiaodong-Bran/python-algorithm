# great common factor
# ʱ�临�Ӷ� >log(N),��ʵֵ2log(N)

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
