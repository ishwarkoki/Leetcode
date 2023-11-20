class Solution:
    def garbageCollection(self, garbage: List[str], time: List[int]) -> int: 

        travel = [[0,0] for _ in range(3)] 
        ans = 0 

        for idx, string in enumerate(garbage): 

            if 'G' in string: 
                travel[0][0] += string.count('G') 
                travel[0][1] = idx 

            if 'P' in string: 
                travel[1][0] += string.count('P') 
                travel[1][1] = idx 

            if 'M' in string: 
                travel[2][0] += string.count('M')  
                travel[2][1] = idx  

        for i in range(1,len(time)): 
            time[i] = time[i] + time[i-1] 


        for count, last_idx in travel: 
            if count > 0:
                ans += count
            if last_idx > 0 : 
                ans += time[last_idx -1]

        return ans 


                

        