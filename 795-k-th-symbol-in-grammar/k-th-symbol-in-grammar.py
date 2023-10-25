class Solution:
    def kthGrammar(self, n: int, k: int) -> int: 
        
        if n ==1 : 
            return 0 

        parent = self.kthGrammar(n-1, math.ceil(k/2)) 
        
        kIsOdd = (k % 2 == 1)  

        if parent == 1 : 
            return 1 if kIsOdd else 0 

        else : 
            return 0 if kIsOdd else 1 
 

                
