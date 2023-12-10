class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]: 

        rows = len(matrix)  
        cols = len(matrix[0]) 
        newMat = [[-1]*rows for _ in range(cols)]  

        for i in range(rows): 
            for j in range(cols):  
                newMat[j][i] = matrix[i][j]

        return newMat 