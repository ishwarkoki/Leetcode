class Solution:
    def minDeletions(self, s: str) -> int:
        smap = {} 
        result = 0 

        for i in s : 
            if i in smap : 
                smap[i] +=1 

            else : smap[i] = 1 

        nums = list(smap.values())

        nums.sort(reverse = True) 

        l, r = 0, 1 

        while r < len(nums): 

            while nums[l] <= nums[r] and nums[r] != 0 : 
                nums[r] -= 1 
                result += 1 

            l ,r = l+1, r+1  

        return result 


        

            

            

    
        