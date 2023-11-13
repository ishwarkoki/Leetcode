class Solution:
    def sortVowels(self, s: str) -> str: 
        vowels = set(['a','e','i','o','u','A','E','I','O','U']) 
        vowelsAscii = [] 
        t = [] 
        i = 0 
        
        for char in s: 
            if char in vowels : 
                vowelsAscii.append(ord(char)) 
                
        vowelsAscii.sort() 
        
        for char in s: 
            if char in vowels: 
                t.append(chr(vowelsAscii[i])) 
                i+=1 
                
            else : 
                t.append(char) 
        
        return "".join(t) 
                
                
            
        