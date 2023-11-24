class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort() 
        ans = 0 

        left, right, right2 = 0, len(piles)-1, len(piles) -2 

        while right > left : 

            ans += piles[right2]

            left += 1 
            right -= 2 
            right2 -= 2 

        return ans 


        