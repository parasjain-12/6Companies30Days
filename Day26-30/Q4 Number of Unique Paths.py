#User function Template for python3

   
class Solution:
    #Function to find total number of unique paths.
    def countUnique(self,a,b,start_row,start_col):
        ans = 0
        dp = [[0 for i in range(b+1)] for j in range(a+1)]
        for i in range(a):
            for j in range(b):
                if i == 0 and j == 0:
                    dp[i][j]=1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[a-1][b-1]
        
    def NumberOfPaths(self,a, b):
        start_row = 0
        start_col = 0
        return self.countUnique(a,b,start_row,start_col)
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends
