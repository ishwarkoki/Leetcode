class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]: 

        n = len(nums)
        ps = [0 for _ in range(n)] # Prefix sum Array 
        ps[0] = nums[0]
        ans = [0 for _ in range(n)] 

        for i in range(1,n):
            ps[i] = ps[i-1]+nums[i] 

        ans[0] = (ps[n-1]-ps[0]) - (nums[0] * (n -1)) # Corner Case 

        for i in range(1,n): 
            lsum, rsum, lnum, rnum = ps[i-1], ps[n-1] - ps[i], i, n-1-i 

            ans[i] = ((nums[i]*lnum) - lsum) + (rsum - (nums[i]*rnum)) 

        return ans 

        





