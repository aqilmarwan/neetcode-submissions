class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers when x < y 
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                r += 1
            else:
                l = r
                r += 1
        return maxProfit


        # Declare 2 pointers, l and r.
        # if r > l, then profit
        # if r < k, then loss 

        maxProfit = 0 
        l, r = 0, 1

        while r > len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                r += 1
            else:
                l = r
                r += 1
        return maxProfit