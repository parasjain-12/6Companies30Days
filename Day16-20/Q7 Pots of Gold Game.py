class Solution:
    def fun(self,dp,arr,start,end):

        if start>end:
            return 0
        if dp[start][end] != 0: return dp[start][end]
        if start<=end and start<len(arr) and end>=0:
            t1 = arr[start] + min(self.fun(dp,arr,start+2,end), self.fun(dp,arr,start+1,end-1))
            t2 = arr[end]+ min(self.fun(dp,arr,start+1,end-1),self.fun(dp,arr,start,end-2))
            dp[start][end] = max(t1,t2)
            return dp[start][end] 
        dp[start][end] = 0
        return 0
    def maxCoins(self,arr, n):
        dp = [[0 for i in range(n+1)] for i in range(n+1)]
        return self.fun(dp,arr,0,n-1)
        # Code here
        
 

#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends
