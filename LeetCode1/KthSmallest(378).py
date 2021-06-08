class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # 8번째로 작다 -> (9 - 8) + 1 -> 2 번째로 크다 -> 인덱스 1이다. 
        idx = len(matrix) ** 2 - k
        all = []
        
        for i in range(len(matrix)):
            all += matrix[i]
        
        all.sort(reverse = True)
        
        return all[idx]