class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]: 

        mp = {} 
        ans = []

        for idx, val in enumerate(groupSizes) : 
            if val not in mp: 
                mp[val] = [] 

            mp[val].append(idx) 

        for key, val in mp.items() : 

            if len(val) == key : 
                ans.append(val) 

            else : 
                count = len(val) 
                group = []  

                while count != -1: 
                    if len(group) == key : 
                        ans.append(group) 
                        group =[] 
                        
                    group.append(val[count-1])
                    count -=1 

        return ans