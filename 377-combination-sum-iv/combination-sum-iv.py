class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int: 

        n = len(nums) 
        dp = [[-1 for _ in range(target+1)] for i in range(len(nums)+1) ] 

        def solve(i, t): 

            if i >= n or t > target : 
                return 0 

            if t == target : 
                return 1 

            

            if dp[i][t] != -1 : 
                return dp[i][t]

            take = solve(0,t+nums[i]) 
            skip = solve(i+1,t) 

            dp[i][t] = take + skip 
            return dp[i][t]

        return solve(0, 0)


        