# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
def maxProfit(prices: List[int]):

    if len(prices) < 2:
        return 0
        
    max_profit = 0
    l, r = 0, 1
    
    while(r < len(prices)):
        if prices[l] > prices[r]:
            l = r
            r +=1
        else:
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
    if max_profit < 0:
        return 0
    return max_profit
