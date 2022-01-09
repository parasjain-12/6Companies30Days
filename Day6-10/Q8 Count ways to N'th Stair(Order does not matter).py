#User function Template for python3

class Solution:
    
    #Function to count number of ways to reach the nth stair 
    #when order does not matter.
    def countWays(self,m):
        temp = m//2
        return temp+1
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends
