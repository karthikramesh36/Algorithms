unsorted=[-1,8,4,8,2,4,0,-5,3,7,6,9]


def quicksort(unsorted):
    quicksort1(unsorted,0,int(len(unsorted))-1)

def getpivot(unsorted,low,high):
    #median of three as pivot
    mid = int(low + high)/2
    pivot = high
    if unsorted[low] < unsorted[mid]:
        if unsorted[mid] < unsorted[high]:
            pivot = mid
    elif unsorted[low] < unsorted[high]:
        pivot = low
    return pivot

def partition(unsorted,low,high):

    pindex = getpivot(unsorted,low,high)
    pvalue= unsorted[pindex]
    temp=unsorted[low]
    unsorted[low]=unsorted[pindex]
    unsorted[pindex]=temp

    border=low
    for i in range(low,high+1):
        if unsorted[i] < pvalue:
            border+=1
            temp1=unsorted[border]
            unsorted[border]=unsorted[i]
            unsorted[i]=temp1

    temp3=unsorted[low]
    unsorted[low]= unsorted[border]
    unsorted[border]=temp3

    return (border)




def quicksort1(unsorted,low,high):
    if low < high:
        p = partition (unsorted,low,high)
        quicksort1(unsorted,low,p-1)
        quicksort1(unsorted,p+1,high)

quicksort(unsorted)
print(unsorted)
