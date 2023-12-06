class Solution:
    def totalMoney(self, n: int) -> int: 
        last_monday = 0 
        ans = 0 

        for i in range(1,n+1): 
            if i%7 == 1 : 
                last_monday += 1 
                money = last_monday 
                
            ans += money 
            money += 1 

        return ans 


             
        