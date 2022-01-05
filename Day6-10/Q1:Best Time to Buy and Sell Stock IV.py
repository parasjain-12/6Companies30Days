class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n==1:
            return 0
        table = [[0 for i in range(n)] for i in range(k+1)]
        for row in range(1,k+1):
            m = 0
            maxdiff = -11111111111111
            for col in range(1,n):
                maxdiff = max(maxdiff,table[row-1][m] - prices[m])
                temp = table[row][col-1]
                temp2 = prices[col] + maxdiff
                table[row][col] = max(temp,temp2)
                m+=1
                

        return table[k][n-1]
