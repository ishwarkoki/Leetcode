class Solution:
    def countHomogenous(self, s: str) -> int: 

        l, r = 0, 0 
        n = 0 
        ans = 0
        mod = 10**9+7  

        while r < len(s): 

            if s[l] == s[r] : 
                r += 1 

            else : 
                n = r-l 
                ans += n*(n+1)//2 # add the homogenity count 

                l = r 

        
        n = r-l 
        ans += n*(n+1)//2 # add the homogenity count 

        ans = ans % mod # to avoid overflow of integer

        return ans 

       
        