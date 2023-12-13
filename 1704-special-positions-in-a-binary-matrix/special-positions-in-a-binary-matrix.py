class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int: 

        ans = 0 
        row, col = len(mat), len(mat[0]) 
        row_sum, col_sum = [ 0 for _ in range(row)], [ 0 for _ in range(col)]

        for i in range(row): 
            for j in range(col): 
                if mat[i][j] == 1 : 
                    row_sum[i] += 1 
                    col_sum[j] += 1 
            
        for i in range(row): 
            for j in range(col): 
                if mat[i][j] == 1 : 
                    if col_sum[j] == 1 and row_sum[i] == 1 : 
                        ans += 1 

        return ans 


         
        