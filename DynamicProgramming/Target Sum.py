# https://leetcode.com/problems/combination-sum-iv/



### Description:
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.




### Examples:
# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Example 2:
# Input: nums = [1], target = 1
# Output: 1




### Solution:
### Level-Order BFS

def findTargetSumWays(self, nums, S):
    count = defaultdict(int)
    count[0] = 1
    for x in nums:
        step = defaultdict(int)
        for y in count:
            step[y + x] += count[y]
            step[y - x] += count[y]
        count = step

    return count[S]
