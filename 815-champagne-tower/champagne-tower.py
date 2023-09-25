class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_row + 1) for _ in range(query_row + 1)]
        dp[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j] += (dp[i][j] - 1) / 2.0
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2.0

        return min(1.0, dp[query_row][query_glass])
