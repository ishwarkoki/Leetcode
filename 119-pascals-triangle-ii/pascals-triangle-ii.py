class Solution:
    def getRow(self, rowIndex: int) -> List[int]: 

        triangle = [] 

        for i in range(rowIndex+1): 
            row = [1]*(i+1) # Fill row with 1's 

            for j in range(1,i): 
                row[j] = triangle[i-1][j-1] + triangle[i-1][j] # change values based on previous row 

            triangle.append(row) 

        return triangle[-1]
        