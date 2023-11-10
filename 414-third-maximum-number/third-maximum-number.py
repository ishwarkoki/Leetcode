class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf') 

        for num in set(nums): 

            if num > max1 : 
                max3, max2, max1 = max2, max1, num 

            elif num > max2 : 
                max3, max2 = max2 , num 

            elif num > max3 : 
                max3 = num 

        sum_ = sum([max1, max2, max3]) 

        return max1 if sum_ == float('-inf') else max3 
        