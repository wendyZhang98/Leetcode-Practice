### Descriptions:
- https://leetcode.com/problems/search-in-rotated-sorted-array/
<img width="1246" alt="Screen Shot 2022-02-23 at 20 02 14" src="https://user-images.githubusercontent.com/49216429/155437090-6cb93e74-d314-42ed-8aa8-a2aecafe6859.png">


### Examples:
<img width="1278" alt="Screen Shot 2022-02-23 at 20 02 29" src="https://user-images.githubusercontent.com/49216429/155437130-cb8634ae-1fe9-4333-a0c6-fdb755b9f95e.png">


### Solutions:
<img width="1094" alt="Screen Shot 2022-02-23 at 20 03 58" src="https://user-images.githubusercontent.com/49216429/155437291-3e7b2ea2-69a0-474a-be24-8fc26d12c37e.png">

<img width="1117" alt="Screen Shot 2022-02-23 at 20 08 06" src="https://user-images.githubusercontent.com/49216429/155437705-bded1c66-d3cf-49cb-afc9-80972ac58c56.png">
<img width="1127" alt="Screen Shot 2022-02-23 at 20 08 18" src="https://user-images.githubusercontent.com/49216429/155437725-b6f54c86-adbb-4e9a-bdb8-2aced7a2b226.png">
<img width="1052" alt="Screen Shot 2022-02-23 at 20 08 42" src="https://user-images.githubusercontent.com/49216429/155437756-04e2dbd4-d289-4210-8f20-a1019419692d.png">

```
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)
```
