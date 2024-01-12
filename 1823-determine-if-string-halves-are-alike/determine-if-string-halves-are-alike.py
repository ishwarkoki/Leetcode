class Solution:
    def halvesAreAlike(self, s: str) -> bool: 

        current_length = 0 
        half_length = len(s)//2
        count = 0   

        for char in s : 
            current_length += 1

            if current_length <= half_length : 
                if char in set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')) :
                    count += 1 

            if current_length > half_length : 
                if char in set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')) :
                    count -= 1 
   
        return count == 0 



        