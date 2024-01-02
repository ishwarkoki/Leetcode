class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]: 
        
        ans = [] 
        used = [False for _ in range(len(nums))] 

        while not all(used): 
            row = [] 
            hashset = set()

            for i in range(len(nums)): 
                if not used[i] and nums[i] not in hashset : 
                    row.append(nums[i]) 
                    used[i] = True 
                    hashset.add(nums[i]) 

            print(row)
                    
            ans.append(row) 

        return ans  

        