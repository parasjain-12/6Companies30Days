#User function Template for python3

class Solution:
    def kvowelwords(self, n,k):
        # code here
        dp= [[0 for  i in range(k+1)] for j in range(n)]
        su = 1
        MOD = 1000000007
        for i in range(n):
            dp[i][0] = (su*21)%MOD
            su = dp[i][0]
            # print(dp[i][0],dp)
            for j in range(1,k+1):
                if j == i+1:
                    dp[i][j] = 5**(i+1)
                elif j>i+1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j-1]*5
                    
                dp[i][j] = dp[i][j]%MOD
                su += dp[i][j]
                su %= MOD
        return su



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N,K = map(int,input().split())
        ob = Solution()
        ans = ob.kvowelwords(N,K)
        print(ans)
# } Driver Code Ends
