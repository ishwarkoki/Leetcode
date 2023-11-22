class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        ans, result = [], [] 

        for row_idx, row in enumerate(nums) : 
            for col_idx, ele in enumerate(row) :  
                result.append((row_idx+col_idx, col_idx, row_idx)) 

        result.sort() 

        for summ, col, row in result : 
            ans.append(nums[row][col]) 

        return ans 



        