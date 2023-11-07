class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int: 

        for i in range(len(dist)):
            dist[i] = (dist[i] - 1) // speed[i]
        dist.sort()
        for i in range(len(dist)):
            if i > dist[i]:
                return i
        return len(dist)
        