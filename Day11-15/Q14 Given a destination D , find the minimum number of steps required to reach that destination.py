#User function Template for python3

class Solution:
    def minSteps(self, n):
        steps = 0
        source = 0
        while source < n:
            steps+=1
            source+=steps

        if source == n or (source-n)%2==0:
            return steps
            
        while (n-source)%2 != 0 :
            steps+=1
            source += steps
        return steps
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        D = int(input())
        
        ob = Solution()
        print(ob.minSteps(D))
# } Driver Code Ends
