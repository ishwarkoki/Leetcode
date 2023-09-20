class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r = 0, 0 
        ans = -1 
        cur_sum = 0 
        n = len(nums)

        req_sum = sum(nums) - x 

        if req_sum < 0 : 
            return -1 

        for r in range(n): 
            cur_sum += nums[r]  # expand the window 

            while l <= r and cur_sum > req_sum : # shrink the window 
                cur_sum -= nums[l] 
                l+=1  

            if cur_sum == req_sum : 
                ans = max(ans, r-l+1) 

        return n - ans if ans != -1 else ans




