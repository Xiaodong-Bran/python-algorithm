# Binary search

# input
# 1) ascending order of number arr
# 2)ATTENTION: also input the left and right index for recusively
# 3) the target value
# Output
# if found, return the index ,else, return -1
def BinarySearch(arr,l,r,x):
    if r>=l:
        mid = l+ (r-l)//2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return BinarySearch(arr,l,mid-1,x)
        else:
             return BinarySearch(arr,mid+1,r,x)

    else:
        return -1


arr = [1,2,3,4,5]
targetX = 4
result = BinarySearch(arr,0,len(arr)-1,targetX)
if result is -1:
    print("Not found")
else:
    print("target value locates at index %d" %(result))
