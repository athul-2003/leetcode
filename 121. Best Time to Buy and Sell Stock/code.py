def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float('inf')
        maxProfit = 0

        for currPrice in prices:
            if currPrice < buyPrice:
                buyPrice = currPrice
            elif currPrice > buyPrice and (currPrice - buyPrice) > maxProfit:
                maxProfit = currPrice - buyPrice

        return maxProfit
