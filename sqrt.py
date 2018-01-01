def sqrt(n,precsion=10e-8):

    low,high=0.0 , max(n,1.0)

    mid = low + high / 2.0
    prev = 0
    while abs(mid-prev)> precision:
        if mid ** 2 > n :
            hi = mid
        else:
            lo = mid
        prev,mid=mid,(low+high)/2.0

    return mid
