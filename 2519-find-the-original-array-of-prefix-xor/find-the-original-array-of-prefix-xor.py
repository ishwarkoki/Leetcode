class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        nums = [1] * len(pref) 

        nums[0] = pref[0] 

        for i in range(1,len(pref)): 
            nums[i] = pref[i] ^ pref [i-1] 

        return nums 
        