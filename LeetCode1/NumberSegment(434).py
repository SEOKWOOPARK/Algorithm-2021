class Solution:
    def countSegments(self, s: str) -> int:
        stringToList = s.split(' ')
        
        return len(stringToList) - stringToList.count('')