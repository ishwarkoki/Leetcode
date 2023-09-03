class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        rows, cols = m, n 
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]  


        def solve(i,j): 
            if i == rows -1 and j == cols -1 : 
                return 1 

            if dp[i][j] != -1 : 
                return dp[i][j] 

            elif i == rows-1 : 
                dp[i][j] = solve(i,j+1)
                return dp[i][j]  


            elif j == cols-1 : 
                dp[i][j] = solve(i+1,j) 
                return dp[i][j] 

            else: 
                dp[i][j] = solve(i+1, j) + solve(i, j+1) 
                return dp[i][j] 

        return solve(0,0) 

             

