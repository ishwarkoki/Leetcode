class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_cost = 0
        
        # Priority queue to store edges of MST
        pq = []
        
        # Initialize with node 0
        visited = [False] * n
        visited[0] = True
        x1, y1 = points[0]
        
        # Add edges from node 0 to all other nodes
        for i in range(1, n):
            x2, y2 = points[i]
            cost = abs(x1 - x2) + abs(y1 - y2)
            heapq.heappush(pq, (cost, 0, i))
            
        while pq:
            
            # Extract minimum edge 
            cost, u, v = heapq.heappop(pq)
            
            # If vertex v is already visited, skip this edge
            if visited[v]:
                continue
                
            # Else add cost to MST  
            mst_cost += cost
            visited[v] = True
            
            # Add edges from v to all its adjacent unvisited nodes
            for i in range(n):
                if not visited[i]:
                    x2, y2 = points[i]
                    c = abs(points[v][0] - x2) + abs(points[v][1] - y2) 
                    heapq.heappush(pq, (c, v, i))
                    
        return mst_cost



        