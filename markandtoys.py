def maximumToys(prices, k):
    prices.sort()
    numToys = 0
    for i in range(len(prices)):
        if k>0:
            k = k-prices[i]
            if k>0:
                numToys = numToys+1
            else:
                break
    return numToys

k= 50
ar = [1, 12, 5, 111, 200, 1000, 10]

print("maximo de bunecos: ",maximumToys(ar,k))