

def mergesort(arr):

    if (len(arr)<2):
        return arr

    mid= int(len(arr)/2)
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left,right)


def merge(left,right):
    result=[]
    i,j=0,0
    while(i<len(left) and j<len(right)):
        if (left[i] <= right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

a=[5,6,7,1,9,3,0,2,5]
print(mergesort(a))
