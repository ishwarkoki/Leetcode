class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0 
        g.sort() 
        s.sort() 
        i, j = 0, 0 

        while i < len(g) and j < len(s) : 

            if s[j] >= g[i] :
                i += 1 

            j += 1 

        return i 


        return ans  
        