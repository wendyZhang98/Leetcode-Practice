### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0121.Best%20Time%20to%20Buy%20and%20Sell%20Stock/README.md


### Description:
# 给定一个数组 prices，它的第i个元素 prices[i] 表示一支给定股票第 i 天的价格
# 你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票
# 返回你可以从这笔交易中获取的最大利润
# 如果你不能获取任何利润，返回 0


### Example:
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：
# 在第 2 天（股票价格=1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5
# 注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；
# 同时，你不能在买入前卖出股票。

# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0


class Solution:
    def maxProfit(self, prices):
        res, mi = 0, prices[0]
        for price in prices[1:]:
            res = max(res, price - mi)
            mi = min(mi, price)
        return res


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
