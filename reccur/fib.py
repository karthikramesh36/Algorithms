def fib_rec(n):
    if n==0 | n==1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_dyn(n):
    n=10
    cache=[None] * (n+1)

    if n ==0 | n ==1:
        return n
    if cache[n] != None:
        return cache[n]
    cache[n]= fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]

def fib_ite(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
