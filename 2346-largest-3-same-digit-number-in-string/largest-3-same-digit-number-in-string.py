class Solution:
    def largestGoodInteger(self, num: str) -> str: 
        ans = ''

        for i in range(2, len(num)): 
            if num[i] == num[i-1] and num[i] == num[i-2]: 
                if ans: 
                    if int(num[i]) > int(ans[0]) : 
                        ans = num[i-2:i+1]  

                else :
                    ans = num[i-2:i+1] 

        return ans 




            

            



        
        