class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            
            for j in range(start, end+1):
                dp[j] = min(dp[j], dp[max(0, i-r)] + 1)
                
        if dp[n] == float('inf'):
            return -1
        
        return dp[n]