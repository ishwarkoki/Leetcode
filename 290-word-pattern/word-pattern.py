class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ') 
        n = len(pattern) 
        if len(words) != n : return False 
        
        mp  = {}
        hmp = {}

        for i in range(n): 
            if mp.get(pattern[i], 0) != 0 and mp[pattern[i]] != words[i] : return False  
            else: mp[pattern[i]] = words[i]   

            if hmp.get(words[i], 0) != 0 and hmp[words[i]] != pattern[i] : return False
            else : hmp[words[i]] = pattern[i]  

        return True 


                


