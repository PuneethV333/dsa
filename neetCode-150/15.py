def maxProfit(prices: list[int]) -> int:
    maxVal = 0
    for i, val in enumerate(prices):
        for j in prices[i + 1 :]:
            if j < val:
                continue
            maxVal = max(maxVal, j - val)
    return maxVal


def maxProfit2(prices: list[int]) -> int:
    minVal = float("inf")
    profit = 0

    for i in prices:
        minVal = min(i, minVal)
        profit = max(profit, i - minVal)

    return profit


print(maxProfit([3, 2, 6, 5, 0, 3]))
