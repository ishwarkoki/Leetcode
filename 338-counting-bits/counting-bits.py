class Solution:
    def countBits(self, n: int) -> List[int]: 
        ans =  []

        def count_ones(num): 
            return bin(num).count('1') 

        for num in range(n+1): 
            ans.append(count_ones(num)) 

        return ans


        