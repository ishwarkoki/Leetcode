class Solution:
    def minOperations(self, nums: List[int]) -> int: 

        c = Counter(nums) 
        ans = 0 

        if min(c.values()) == 1 : return -1 

        for num in c.values(): 

            ans += ceil(num/3) 

        return ans 
        