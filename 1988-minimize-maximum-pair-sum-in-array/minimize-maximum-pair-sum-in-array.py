class Solution:
    def minPairSum(self, nums: List[int]) -> int: 

        nums.sort() 
        start, end = 0, len(nums)-1 
        maxPair = -1 


        while start < end :  
            if nums[start] + nums[end] > maxPair : 
                maxPair = nums[start] + nums[end] 

            start +=1 
            end -= 1

        return maxPair 


        