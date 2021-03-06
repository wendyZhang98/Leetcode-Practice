### Description:
- Given an integer array nums and an integer k, 
- return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

### Examples:
<img width="646" alt="Screen Shot 2022-02-13 at 00 10 39" src="https://user-images.githubusercontent.com/49216429/153739653-c9e8de62-170d-4367-ab65-1ed23f021130.png">


### Solutions:

<img width="1261" alt="Screen Shot 2022-02-23 at 19 10 57" src="https://user-images.githubusercontent.com/49216429/155432199-71a80246-033e-4625-8cc2-11d29e994962.png">
<img width="1094" alt="Screen Shot 2022-02-23 at 19 12 01" src="https://user-images.githubusercontent.com/49216429/155432309-22351ce3-8a17-4c07-855a-21251eb509c2.png">
<img width="1096" alt="Screen Shot 2022-02-23 at 19 12 12" src="https://user-images.githubusercontent.com/49216429/155432335-592e3daa-1b6c-415b-bae1-961f0dd7087f.png">
<img width="1092" alt="Screen Shot 2022-02-23 at 19 18 37" src="https://user-images.githubusercontent.com/49216429/155432949-dd0ffdc6-517d-4af4-b83d-c8ecd8ad5c46.png">
<img width="1083" alt="Screen Shot 2022-02-23 at 19 12 56" src="https://user-images.githubusercontent.com/49216429/155432404-2305f6d8-ca06-4b79-bd66-ca934374c8e3.png">
<img width="1098" alt="Screen Shot 2022-02-23 at 19 13 06" src="https://user-images.githubusercontent.com/49216429/155432426-fbb2f79b-69a7-4577-8ae0-b258029276eb.png">
<img width="1100" alt="Screen Shot 2022-02-23 at 19 13 17" src="https://user-images.githubusercontent.com/49216429/155432442-4bf77b54-0029-4324-bb70-977d1e202a16.png">
<img width="1077" alt="Screen Shot 2022-02-23 at 19 13 30" src="https://user-images.githubusercontent.com/49216429/155432463-2fbeed51-d2e6-4e5b-b73a-511e73fd0f34.png">
<img width="1091" alt="Screen Shot 2022-02-23 at 19 14 10" src="https://user-images.githubusercontent.com/49216429/155432524-e0557fe7-b893-4185-a77e-8775eca113ac.png">
<img width="1283" alt="Screen Shot 2022-02-23 at 19 16 55" src="https://user-images.githubusercontent.com/49216429/155432799-5f661b28-82b3-4da2-987e-4a0342ef1f26.png">

```
class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
    
        # If the total sum is not divisible by k, we can't make subsets.
        total_array_sum = sum(arr)
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        taken = [False] * n
        
        def backtrack(index, count, curr_sum):
            n = len(arr)
      
            # We made k - 1 subsets with target_sum and the last subset must also have target_sum.
            if count == k - 1:
                return True
            
            # No need to proceed further.
            if curr_sum > target_sum:
                return False
                
            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                return backtrack(0, count + 1, 0)
                
            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if not taken[j]:
                    # Include this element in current subset.
                    taken[j] = True
                    
                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True
        
                    # Backtrack step.
                    taken[j] = False
    
            # We were not able to make a valid combination after picking 
            # each element from the array, hence we can't make k subsets.
            return False
        
        return backtrack(0, 0, 0)
```
