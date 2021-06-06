from collections import deque

class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ''
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U']
        reverse = deque([])
        
        for i in range(len(s) - 1,  -1, -1):
            if vowels.count(s[i]) == 1:
                reverse.append(s[i])
        
        for i in range(len(s)):
            if vowels.count(s[i]) == 0:
                result += s[i]
            else:
                result += reverse[0]
                reverse.popleft()
        
        return result