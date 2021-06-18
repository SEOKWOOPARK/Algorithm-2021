class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            if len(stones) == 2:
                sub = stones[0] - stones[1]
                if sub == 0:
                    return 0
                else:
                    return abs(sub)
            
            stones.sort()
            sub = stones[len(stones) - 1] - stones[len(stones) - 2]
            
            if sub == 0:
                stones = stones[:len(stones) - 2]
            else:
                stones = stones[:len(stones) - 2]
                stones.append(abs(sub))
                        
        return stones[0]