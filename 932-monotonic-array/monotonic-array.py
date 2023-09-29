class Solution:
    def isMonotonic(self, nums: List[int]) -> bool: 
        n = len(nums) 

        increasing = decreasing = False 

        for i in range(1,n): 
            if nums[i] > nums[i-1]: 
                increasing = True 

            elif nums[i] < nums[i-1]: 
                decreasing = True 

        if increasing and decreasing : return False 
        else : return True 



          
        