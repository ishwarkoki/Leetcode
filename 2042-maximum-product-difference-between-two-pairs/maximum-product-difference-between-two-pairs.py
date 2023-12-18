class Solution:
    def maxProductDifference(self, nums: List[int]) -> int: 

        max1, max2, min1, min2 = 0, 0, 10**4 + 1, 10**4 + 1

        for num in nums: 
            if num > max1 : 
                max2 = max1
                max1 = num

            elif num > max2 : 
                max2 = num 
                 
            if num < min1 : 
                min2 = min1
                min1 = num 
            
            elif num < min2 : 
                min2 = num
                
        print(max2, max1, min2, min1)
        return max2*max1 - min2*min1 


