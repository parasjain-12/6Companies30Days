#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        i = 0
        ans = []
        temp = []
        for i in range(k):
            if len(temp) == 0:
                temp.append(arr[i])
            elif arr[i]<temp[-1]:
                temp.append(arr[i])
            else:
                while len(temp)>0 and arr[i]>temp[-1]:
                    temp.pop()
                    
                temp.append(arr[i])
                
        ans.append(temp[0])
        
        i = 0
        for j in range(k,n):
            if arr[i]==temp[0]:
                temp.pop(0)
            i+=1
            if len(temp) == 0:
                temp.append(arr[j])
            elif arr[j]<temp[-1]:
                temp.append(arr[j])
                
            else:
                while len(temp)>0 and arr[j]>temp[-1]:
                    temp.pop()
                temp.append(arr[j])
            ans.append(temp[0])
            
        return ans
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
