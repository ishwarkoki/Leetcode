class Solution:
    def isMonotonic(self, nums: List[int]) -> bool: 
        n = len(nums) 

        def increasing(nums): 
            for i in range(1,n): 
                if nums[i] < nums[i-1] : 
                    return False 

            return True
 

        def decreasing(nums): 
            for i in range(1,n): 
                if nums[i] > nums[i-1] : 
                    return False 

            return True

        return increasing(nums) or decreasing(nums)  
        