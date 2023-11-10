class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]: 

        adj = defaultdict(list) 
        ans = [] 

        for u,v in adjacentPairs : # create the adjacency List/ map
            adj[u].append(v) 
            adj[v].append(u) 

        for key,value in adj.items() : # get the starting point of the List
            if len(value) == 1 : 
                start = key

        def dfs(start, prev): # DFS Traversal using a Prev flag 
            ans.append(start) 

            for val in adj[start] : 
                if val != prev : 
                    dfs(val, start) 

        dfs(start, float('-inf')) 

        return ans 

            

                


            

        



        