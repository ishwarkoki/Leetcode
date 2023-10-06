class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [-1] * (n+1)
        
        def solve(n, dp): 

            ans = -1  

            if dp[n] != -1 : 
                return dp[n] 

            if n == 1 or n ==2 : 
                return 1 

            for i in range(1,n): 
                ans = max(ans, i* (n-i), i* solve(n-i,dp))
        
            dp[n] = ans 
            return dp[n] 

        return solve(n, dp) 
    


 

     



    


       