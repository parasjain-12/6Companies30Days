#User function Template for python3
class Solution:
    def minDifference(self, arr, n):
        su =  sum(arr)
        dp = [[0 for i in range(su+1)] for j in range(len(arr)+1)]
        for i in range(len(arr)+1):
            dp[i][0] = True
            
        for i in range(1,len(arr)+1):
            for j in range(1,su+1):
                if arr[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                    
        li = []
        for i in range(su+1):
            if dp[len(arr)][i] == True:
                li.append(i)
                
        mi = 11111111111111
        for i in range(len(li)//2 +1):
        #     print(2*li[i])
            temp = abs(su - 2*li[i])
            mi = min(mi,temp)
            
        return mi
     
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDifference(arr, N)
        print(ans)

# } Driver Code Ends
