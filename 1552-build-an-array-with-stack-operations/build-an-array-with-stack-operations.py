class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]: 
        j = 0 
        length = len(target)
        ans = []
        
        for i in range(1,n+1): 
            if j < length : 
                if i == target[j] : 
                    ans.append("Push") 
                    j+=1 
                else  : 
                    ans.append("Push")
                    ans.append("Pop")

            else : break 

        return ans 

            


        