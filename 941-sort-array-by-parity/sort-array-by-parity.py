class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]: 
        l, r = 0, len(nums)-1 
        result = [-1]*len(nums)

        for num in nums : 
            if num % 2 == 0 : 
                result[l] = num
                l += 1 
                
            else : 
                result[r] = num
                r -= 1 
                
        return result 
        