class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = prices[-1]
        temp = [0] * (len(prices) - 1)

        profit = 0
        for i in range(len(temp) - 1, -1, -1):
            temp[i] = mx
            if prices[i] > mx:
                mx = prices[i]


        mx = 0
        for i in range(len(prices) - 1):
            tProfit = temp[i] - prices[i]

            if tProfit > mx:
                profit = tProfit
                mx = profit

        return profit if profit > 0 else 0