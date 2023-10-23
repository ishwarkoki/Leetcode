class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0: return False
        
        num = math.log10(n)/math.log10(4) 
        if math.ceil(num)==math.floor(num): return True 
        else: return False
        