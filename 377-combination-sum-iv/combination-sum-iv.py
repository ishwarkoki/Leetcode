class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int: 

        n = len(nums) 
        dp = {} 

        def solve(i, t): 

            if i >= n : 
                return 0 

            if t == target : 
                return 1 

            if t > target : 
                return 0  

            if (i, t) in dp : 
                return dp[(i,t)]

            take = solve(0,t+nums[i]) 
            skip = solve(i+1,t) 

            dp[(i, t)] = take + skip 
            return dp[(i, t)]

        return solve(0, 0)


        