
"""
    So return the largest profit by buying and selling within the days range.
    1. Find the lowest price and set it as the min
    2. Find the highest profit starting at the min price
"""
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 1:
        return 0
    
    min  = prices[0]
    profit = 0
    
    for i in range(1, len(prices)):
        if min > prices[i]:
            min = prices[i]
        else:
            x = prices[i]-min
            if x > profit:
                profit = x
    return profit
    
        