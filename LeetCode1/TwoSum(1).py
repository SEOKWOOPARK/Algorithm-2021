class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            otherNumber = target - nums[i]
            existance = nums.count(otherNumber)
            
            if existance:
                idx = nums.index(otherNumber)
                if (idx > -1) and (idx != i):
                    return [i, idx]