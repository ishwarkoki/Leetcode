class Solution:
    def minOperations(self, nums: List[int]) -> int: 

        c = Counter(nums) 
        ans = 0 

        for num in c.values(): 
            
            if num == 1 : return -1 

            ans += ceil(num/3) 

        return ans 
        