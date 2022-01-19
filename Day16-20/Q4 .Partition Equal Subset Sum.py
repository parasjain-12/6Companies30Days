# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        su = sum(arr)
        if su%2 != 0:
            return 0
        su  = sum(arr)
        dp = [[0 for i in range(su+1)] for j in range(len(arr)+1)]
        for i in range(len(arr)+1):
            dp[i][0] = True
        
            
        for i in range(1,len(arr)+1):
            for j in range(1,su+1):
                if arr[i-1]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                    
        if dp[N][su//2] == True:
            return 1
        return 0
        # code here

#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends
