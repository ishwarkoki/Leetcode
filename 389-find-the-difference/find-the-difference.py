class Solution:
    def findTheDifference(self, s: str, t: str) -> str: 
        sum1 = sum2 = 0 

        for c in t : 
            sum1+= ord(c) 
        for c in s : 
            sum2+= ord(c) 

        diff = sum1 - sum2 

        return chr(diff)



        

                
        
        