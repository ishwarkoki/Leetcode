class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob, n = 0,0, len(colors) 

        for i in range(1, n-1):
            if colors[i] == colors[i-1] and colors[i] == colors[i+1] : 
                if colors[i] == 'A': 
                    alice +=1 

                else : 
                    bob +=1 

        return alice > bob 
        