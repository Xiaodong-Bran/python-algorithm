
# bubbleSort with python

def bubbleSort(Mylist):
    # input a list
    # return a list with decreasing order
    n = len(Mylist)
    # print(n)
    for i in range(0,n-1):
        # outside loop from Mylist[0] to Mylist[n-2]
        for j in range(i+1,n):
         # inside loop from Mylist[i+1] to Mylist[n-1] /
         # n-1 is the last element in the list
            if Mylist[i] > Mylist[j]:
                temp = Mylist[i]
                Mylist[i] = Mylist[j]
                Mylist[j] = temp
    return Mylist

print(bubbleSort([15,12,10,4,6,17]))
