class Solution:
    def bs(self, nums): 
        lo, hi = 0, len(nums)-1 
        res = -1 

        while lo<=hi : 
            mid = lo + (hi-lo)//2 

            if nums[mid] == 1 : 
                res = mid 
                lo = mid + 1 

            else : 
                hi = mid-1 

        return 0 if res == -1 else res+1 

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:  

        min_heap = []
        ans = []

        for i in range(len(mat)): 
            heapq.heappush(min_heap,(self.bs(mat[i]),i))  

        for _ in range(k): 
            sum_, idx = heapq.heappop(min_heap)
            ans.append(idx) 

        return ans  


        # n * log(n)




        