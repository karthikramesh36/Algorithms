import random

def euclidean_distance(n):
    if n < 0:
        print("invalid input")
        return -1
    #start point at [0,0]
    # use random to choose x/y axis to eitehr increment or decrement
    start = [0,0]
    count = 0
    while count < n:
        choose_y,choose_x = False, False

        if random.choice((True,False)):
            choose_y = True
        else:
            choose_x = True
        if choose_y:
            if random.choice((True,False)):
                start[1] += 1
            else:
                start[1] -= 1
        elif choose_x:
            if random.choice((True,False)):
                start[0] += 1
            else:
                start[0] -=1
        count +=1
        print(start)
    #to calculate euclidean_distance we must find absolute value of end point
#    start[0] = abs(start[0])
#    start[1] = abs(start[1])

    distance = ((abs(start[0])-0)**2 + (abs(start[1])-0)**2)**(1/2.0)
    print("euclidean distance: ",distance)

euclidean_distance(-1)
