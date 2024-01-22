class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]: 
        
        n = len(nums) 
        set_sum = sum(set(nums))

        missing_num = sum(range(1, n+1)) - set_sum
        duplicated_num = sum(nums) - set_sum

        return [duplicated_num, missing_num]

         

        
        