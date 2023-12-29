class Solution:
   def __init__(self):
       # Initialize memoization table with dimensions matching C++ code
       self.t = [[-1] * 11 for _ in range(301)]

   def solve(self, jobDifficulty, n, idx, d):
       """
       Recursive function to find the minimum difficulty to schedule jobs.
       """

       if d == 1:
           # If only one day left, return the maximum difficulty among remaining jobs
           return max(jobDifficulty[idx:])

       if self.t[idx][d] != -1:
           # Memoization: return cached result if available
           return self.t[idx][d]

       max_difficulty = float('-inf')
       result = float('inf')

       # Iterate through possible job assignments for the current day
       for i in range(idx, n - d + 1):
           max_difficulty = max(max_difficulty, jobDifficulty[i])
           result = min(result, max_difficulty + self.solve(jobDifficulty, n, i + 1, d - 1))

       self.t[idx][d] = result  # Store result for memoization
       return result

   def minDifficulty(self, jobDifficulty, d: int) -> int:
       """
       Main function to find the minimum difficulty to schedule jobs.
       """

       n = len(jobDifficulty)

       if n < d:
           return -1

       return self.solve(jobDifficulty, n, 0, d)
