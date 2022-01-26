class Solution:
    def stoneGame(self, piles):
        n = len(piles)
        dp = [[None] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i] 
        for row in range(n-1, -1, -1):
            for col in range(row+1, n):
                dp[row][col] = sum(piles[row:col+1]) - min(dp[row+1][col], dp[row][col-1])
        return dp[0][n-1] >= max(dp[1][n-1], dp[0][n-2])
