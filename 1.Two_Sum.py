#Brute Force Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if target == nums[i]+nums[j]:
                    return [i,j]
        return []
        
#Best Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i
        return []