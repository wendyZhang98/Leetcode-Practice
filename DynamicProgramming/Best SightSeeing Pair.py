### Link:
# https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1014.Best%20Sightseeing%20Pair/README.md


### Description:
# 给你一个正整数数组 values，其中values[i]表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i
# 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离
# 返回一对观光景点能取得的最高分


### Example:
# 输入：values = [8, 1, 5, 2, 6]
# 输出：11
# 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

# 输入：values = [1, 2]
# 输出：2


class Solution:
    def maxScoreSightseeingPair(self, values):
        res, mx = 0, values[0]
        for i in range(1, len(values)):
            res = max(res, values[i]-i+mx) # whether to set j
            mx = max(mx, values[i]+i) # whether to set i
        return res

    
print(Solution().maxScoreSightseeingPair(values = [8, 1, 5, 2, 6]))
