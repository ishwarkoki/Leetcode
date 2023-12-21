class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int: 
        x_axis = [] 
        max_width = 0 

        for x,y in points : 
            x_axis.append(x)  

        x_axis.sort() 

        for i in range(1,len(x_axis)) : 
            max_width = max(max_width, x_axis[i]-x_axis[i-1]) 

        return max_width 

        