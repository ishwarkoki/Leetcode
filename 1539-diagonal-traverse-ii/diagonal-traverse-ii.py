class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        mp = defaultdict(list)
        ans = []

        for i in reversed(range(len(nums))): 
            for j in range(len(nums[i])): 
                mp[i+j].append(nums[i][j]) 

        for i in range(len(mp.keys())) : 
            for num in mp[i] : 
                ans.append(num) 

        return ans 




        