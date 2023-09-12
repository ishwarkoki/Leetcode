class Solution:
    def minDeletions(self, s: str) -> int:
        smap = {} 
        result = 0 

        for i in s : 
            if i in smap : 
                smap[i] +=1 

            else : smap[i] = 1 

        nums = list(smap.values())
        
        seen = set() 

        for i in range(len(nums)) : 

            while nums[i] and nums[i] in seen : 
                nums[i] -=1 
                result += 1 

            else : 
                seen.add(nums[i]) 

        return result 




        # Time : O(N) + O(KlogK) + O(K**2) 
        # Space : O(N) 
         

            

            

    
        