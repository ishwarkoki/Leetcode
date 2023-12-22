class Solution:
    def maxScore(self, s: str) -> int:  
        n = len(s)
        left, right, maxScore = 0, 0, 0 

        for i in range(1,n): 
            left  =  s[:i].count('0')
            right =  s[i:].count('1')

            maxScore = max(maxScore, left+right) 

        return maxScore 

        