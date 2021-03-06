# Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0189.Rotate%20Array/README.md


### Description:
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的原地算法解决这个问题吗？


### Example:
# 示例1:
# 输入: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# 输出: [5, 6, 7, 1, 2, 3, 4]
# 解释: 向右旋转
# 1步: [7, 1, 2, 3, 4, 5, 6] 向右旋转
# 2步: [6, 7, 1, 2, 3, 4, 5] 向右旋转
# 3步: [5, 6, 7, 1, 2, 3, 4]

# 示例2:
# 输入：nums = [-1, -100, 3, 99], k = 2
# 输出：[3, 99, -1, -100]
# 解释: 向右旋转
# 1 步: [99, -1, -100, 3] 向右旋转
# 2 步: [3, 99, -1, -100]

# 提示：
# 1 <= nums.length <= 2 * 104
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105


### Solution：
# 若 k = 3，nums = [1, 2, 3, 4, 5, 6, 7]
# 先将 nums 整体翻转：[1, 2, 3, 4, 5, 6, 7] -> [7, 6, 5, 4, 3, 2, 1]
# 再翻转 0 ~ k - 1 范围内的元素：[7, 6, 5, 4, 3, 2, 1] -> [5, 6, 7, 4, 3, 2, 1]
# 最后翻转 k~ n - 1 范围内的元素，即可得到最终结果：[5, 6, 7, 4, 3, 2, 1] -> [5, 6, 7, 1, 2, 3, 4]


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything,
        modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if n < 2 or k == 0:
            return
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

        return nums
      
print(Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=4))
