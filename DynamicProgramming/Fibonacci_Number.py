### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0500-0599/0509.Fibonacci%20Number/README_EN.md


### Description:
# 斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列
# 该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和
# 也就是：
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 给你 n ，请计算 F(n)


### Example
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1

# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2

# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3


class Solution:
    def fibonacci(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


print(Solution().fibonacci(n=10))