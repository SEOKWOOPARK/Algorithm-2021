class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {}
        length = len(nums)
        zero = 0
        twice = 0
        
        for i in range(length):
            dic[i + 1] = 0
        
        for i in range(length):
            dic[nums[i]] += 1
                                    
        # 2번 나온 num이랑 0번 나온 num 찾기
        dic = list(dic.items())
    
        for i in range(len(dic)):
            if dic[i][1] == 2:
                twice = dic[i][0]
                
            if dic[i][1] == 0:
                zero = dic[i][0]
        
        return [twice, zero]