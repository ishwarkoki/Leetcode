# O(N logN ) solution 
class Solution:
    def countBits(self, n: int) -> List[int]: 
        ans =  []

        def count_ones(num): 
            return bin(num).count('1') 

        for num in range(n+1): 
            ans.append(count_ones(num)) 

        return ans

# O(N)  solution
class Solution:
    def countBits(self, n: int) -> List[int]: 
        ans =  [None] * (n+1) 

        ans[0] = 0 

        for num in range(n+1): 

            if num%2 == 0 : 
                ans[num] = ans[num//2] 
            else : 
                ans[num] = ans[num//2]+1 

        return ans 

# A number is expressed as : 
# half_number<<1 if number is even  
# (half_number<<1) +1 if number is odd
# And we know that left shift will add just a zero at end, so same number of bits as half_number if even and add one more bit if odd
 

        


        
