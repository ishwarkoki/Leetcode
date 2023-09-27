class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str: 

        total_length = 0 


        for i in s : 
            if i.isdigit(): 
                total_length *= int(i) 

            else : 
                total_length += 1  

        for i in reversed(s): 
            k %= total_length 

            if k == 0 and i.isalpha(): 
                return i 

            if i.isdigit(): 
                total_length /= int(i) 

            else : 
                total_length -= 1 

            
            


        
        