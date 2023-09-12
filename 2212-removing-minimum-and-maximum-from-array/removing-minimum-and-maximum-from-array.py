class Solution:
    def minimumDeletions(self, nums: List[int]) -> int: 

        mini_index , maxi_index = -1, -1 
        mini, maxi = 1e5 +1 , -(1e5 +1) 

        for i in range(len(nums)): 
            if nums[i] > maxi : 
                maxi = nums[i] 
                maxi_index = i 

            if nums[i] < mini : 
                mini = nums[i] 
                mini_index = i 

        # min -> min(mini_index, maxi_index), max -> max(mini_index, maxi_index)  

        minimum_index, maximum_index  = min(mini_index, maxi_index), max(mini_index, maxi_index)
        ele1, ele2, ele3  = ((minimum_index - 0 + 1 ) + (len(nums)-maximum_index)), (maximum_index-0 + 1), len(nums) - minimum_index

        return min(ele1, ele2, ele3) 

            
        