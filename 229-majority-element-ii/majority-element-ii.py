class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
        counter = {} 
        n = len(nums)
        ans = []

        for num in nums: 
            counter[num] = counter.get(num, 0) + 1 

        for key, count in counter.items(): 
            if count > n/3 : 
                ans.append(key) 

        return ans 

            
         