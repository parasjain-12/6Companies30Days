#User function Template for python3


class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,arr,n):
        st = []
        ans = []
        for i in range(len(arr)):
            # print(st)
            if len(st)==0:
                st.append(i)
                ans.append(1)
                
            elif arr[st[-1]]>arr[i]:
                st.append(i)
                ans.append(1)
            else:
                while len(st)>0 and arr[st[-1]]<=arr[i]:
                    st.pop()
                    
                if len(st)>0:
                    ans.append(i-st[-1])
                else:
                    ans.append(i+1)
                    
                st.append(i)
                
        return ans
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

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
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        print(*ans) # print space seperated elements of span array
# } Driver Code Ends
