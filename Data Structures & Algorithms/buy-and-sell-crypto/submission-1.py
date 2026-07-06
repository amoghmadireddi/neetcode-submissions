class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0
        for i in range(1, len(prices)):
            current = prices[i] - lowest
            best = max(best, current)
            lowest = min(prices[i], lowest)
        return best