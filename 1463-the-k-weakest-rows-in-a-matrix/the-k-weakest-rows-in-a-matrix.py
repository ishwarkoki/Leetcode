class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:  

        min_heap = []
        ans = []

        for i in range(len(mat)): 
            heapq.heappush(min_heap,(sum(mat[i]),i)) 

        for _ in range(k): 
            sum_, idx = heapq.heappop(min_heap)
            ans.append(idx) 

        return ans




        