#User function Template for python3

class Solution:
    def height(self, N):
        # code here
        import math
        temp = (-1 + math.sqrt(1+8*N))//2
        return int(temp)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.height(N))
# } Driver Code Ends
