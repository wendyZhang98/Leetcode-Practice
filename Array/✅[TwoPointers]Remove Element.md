### Description:
- https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0027.Remove%20Element/README.md
- 给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，并返回移除后数组的新长度。
- 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
- 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


### Example:
#1
- Input: nums = [3,2,2,3], val = 3
- Output: 2, nums = [2,2]

#2
- Input: nums = [0,1,2,2,3,0,4,2], val = 2
- Output: 5, nums = [0,1,4,0,3]


### Solution:
- 由于题目要求删除数组中等于 val 的元素，因此输出数组的长度一定小于等于输入数组的长度, 我们可以把输出的数组直接写在输入数组上
- 右指针 right 指向当前将要处理的元素; 左指针 left 指向下一个将要赋值的位置
- 如果右指针指向的元素不等于 val, 它一定是输出数组的一个元素; 我们就将右指针指向的元素复制到左指针位置，然后将左右指针同时右移
- 如果右指针指向的元素等于 val, 它不能在输出数组里; 此时左指针不动，右指针右移一位
- 整个过程保持不变的性质是：区间 0,left 中的元素都不等于 val
- 当左右指针遍历完输入数组以后，left 的值就是输出数组的长度
```
class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        lst = nums[:left]
        print(lst)
        return left

print(Solution().removeElement(nums=[1,2,2,3,4,5,8], val=2))
```
