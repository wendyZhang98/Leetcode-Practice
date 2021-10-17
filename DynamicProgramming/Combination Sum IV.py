### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0377.Combination%20Sum%20IV/README.md




### Description:
# 给你一个由 不同 整数组成的数组 nums, 和一个目标整数 target
# 请你从 nums 中找出并返回总和为 target 的元素组合的个数
# 题目数据保证答案符合 32 位整数范围

# 进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？




### Example:
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。

# 输入：nums = [9], target = 3
# 输出：0




### Solution:
# 动态规划
# dp[i]表示总和为i的元素组合的个数

class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]

