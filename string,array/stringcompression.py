def stringcomp(a):
    compress=[]
    counter=0
    for i in range(len(a)):
        if i !=0 and a[i] != a[i-1]:
            compress.append(a[i-1] + str(counter))
            counter=0
        counter+=1

    #add last char
    compress.append(a[-1] + str(counter))

    return ''.join(compress)
# for minimun of 2 string return min(above statement,a,key=len)

a="aaabbbccdddd"
print(stringcomp(a))
