class Solution:
    def getWinner(self, nums: List[int], k: int) -> int:  

        n = len(nums) 
        count = 0 

        left, right = 0, 1 

        if k == 1 : return max(nums[0], nums[1]) 


        while right < n : 

            if nums[left] > nums[right]: 
                count += 1 
                right += 1 

            else : 
                nums[left], nums[right] = nums[right], nums[left] 
                count = 1 
                right += 1 

            if count == k : break

        return nums[left] 
        


        