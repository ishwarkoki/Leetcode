class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            l,r =i,i        
            while l>=0 and r<len(s) and s[l]==s[r]: 
                l-=1;r+=1
            res=max(s[l+1:r], res, key=len)
            
            
            l,r =i,i+1        
            while l>=0 and r<len(s) and s[l]==s[r]: 
                l-=1;r+=1 
            res=max(s[l+1:r], res, key=len)
            
        return res
        
        
        
        
        
        
# Solution if max substring lengh is asked  -> 
#         maxLength =1
#         for i in range(len(s)):
#             l,r,length =i,i,0         
#             while l>=0 and r<len(s) and s[l]==s[r]: 
#                 l-=1;r+=1;length+=1 
#             maxLength =max(maxLength,length) 
            
#             l,r,length =i,i,1         
#             while l>=0 and r<len(s) and s[l]==s[r]: 
#                 l-=1;r+=1;length+=1 
#             maxLength =max(maxLength,length) 
#         return maxLength 
    
    
            
             
                
                
            
        
        
#         # res=0
#         for i in range(len(s)):   
#             res+= self.helper(s,i,i) # strings with odd len 
#             res+= self.helper(s,i,i+1) # strings with even len 
#         return res 
            
#     def helper(self,s,l,r):
#         # count=0
#         while l>=0 and r<len(s) and s[l]==s[r]: 
#             maxLen = max(maxLen,len(s))
#             l-=1 ; r+=1 
#         return count
                
                
        
        
        # O(n2) solution will work - 1< s.length <=10^3 
        # basic Approach find all substrings which are palindrome 
        # return the longest One 
        