class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        newNums = [i for i in set(nums)] 
        newNums.sort()
        
        if len(newNums) < 3 : 
            return max(newNums) 

        else : 
            return newNums[-3] 
        