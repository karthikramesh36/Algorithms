# this code prints out only the possiible combinations and not the coin denominations


#create a combination array with index as 1,2,3,...upto n
# where n is the amount / given input to find possile coin combinations
# so the array at each position holds the possible combinations for that index
# loop through every coin
# for each coin , check combinations from previous index value
# start out with combinations[0] i.e. the first index has value 1
def change(n,coins):

    combinations = [0 for s in range(0,n+1)]
    combinations[0] =1
    for coin in coins:
        for amount in range(1,n+1):
            if amount >= coin:
                combinations[amount] += combinations[amount-coin]
                amount+=1

    return combinations[n]

n = 25
coins = [1, 5, 10, 25]

print(change(n,coins))
