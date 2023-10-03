class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int: 
        counter = {} 
        ans = 0 

        for num in nums : 
            counter[num] = counter.get(num, 0) + 1 

        for key, value in counter.items() : 
            if value > 1 : 
                ans += math.comb(value, 2)

        return ans 

            




         