

def taxycab(n):

    i = 1.0
    count = 0

    while count < n:
        found = 0
        j = 1
        k = j + 1
        limit = i ** (1.0/3)
        for j in range(int(limit)):
            for k in range(int(limit)):
                #check if (j,k)'s cube power sum is equal to i
                if((j*j*j) + (k*k*k)) == i:
                    found += 1
                j+=1
                k+=1
        if found == 2:
            count+=1
            print( count , "  ", i)
        i+= 1

n=4
taxycab(n)
