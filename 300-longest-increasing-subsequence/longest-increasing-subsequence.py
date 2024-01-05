import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        ans = [nums[0]]

        for i in range(1,len(nums)): 
            if nums[i] > ans[-1] : 
                ans.append(nums[i]) 

            else: 
                idx = bisect.bisect_left(ans, nums[i])  # Lower Bound idx  
                ans[idx] = nums[i] 

        return len(ans) 



             


            
