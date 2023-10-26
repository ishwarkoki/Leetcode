class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int: 
        MOD = 10**9 + 7
        arr.sort()
        N = len(arr)
        dp = [1] * N  # Initialize each element to 1

        index = {x: i for i, x in enumerate(arr)}

        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    y = x // arr[j]
                    if y in index:
                        dp[i] += dp[j] * dp[index[y]]
                        dp[i] %= MOD

        return sum(dp) % MOD






        