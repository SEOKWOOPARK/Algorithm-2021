from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k = collections.Counter(nums).most_common()
        
        return k[0][0]
