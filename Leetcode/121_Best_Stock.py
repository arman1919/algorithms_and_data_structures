# incomplete solution

def maxSubArray(prices: list[int]) -> int:
    lenght = len(prices)
    
    max_prices = 0
    for i in range(lenght):
        for j in range(i,lenght):
            if prices[j] - prices[i] > max_prices:
                max_prices =  prices[j] - prices[i]
    
    return max_prices


prices = [7,6,4,3,1]
print(maxSubArray(prices))

prices =[7,1,5,3,6,4]
print(maxSubArray(prices))