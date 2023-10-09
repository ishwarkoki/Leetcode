class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ls = []
        for i in range(len(nums)):
            if nums[i] == target:
                ls.append(i) 

        if len(ls)>0:
            loc=[min(ls),max(ls)]
            return loc 
        else:
            return [-1,-1]





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
        
        res=[]; n=len(nums)
        if target in nums:
            for i,num in enumerate(nums):
                if num==target :
                    num[i-1].isnumeric()
                    res.append(i)
                if num==target and (nums[i+1] !=target or i+1 ==n ): res.append(i)
            return res
        return [-1,-1] 
'''