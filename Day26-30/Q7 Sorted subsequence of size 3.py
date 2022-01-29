#User function Template for python3



class Solution:

    def find3number(self,A, n):
        
        # code here
        smallest = []
        smallest.append(arr[0])
        for i in range(1,len(arr)):
            if smallest[-1]> arr[i]:
                smallest.append(arr[i])
            else:
                smallest.append(smallest[-1])
            
        largest = [0]*len(arr)
        largest[len(arr)-1] = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            if largest[i+1] < arr[i]:
                largest[i] = arr[i]
            else:
                largest[i] = largest[i+1]
                
        ans = []
        for i in range(1,len(arr)-1):
            if smallest[i-1]<arr[i]<largest[i+1]:
                ans.append(smallest[i-1])
                ans.append(arr[i])
                ans.append(largest[i+1])
                break
                
        return ans
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)

def isSubSeq(arr, lis, n, m):
    if m==0:
        return True
    if n==0:
        return False
    if arr[n-1]==lis[m-1]:
        return isSubSeq(arr, lis, n-1, m-1)
    return isSubSeq(arr, lis, n-1, m)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    lis = Solution().find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis)!=0 and len(lis)!=3:
        print(-1)
        continue
    if len(lis)==0:
        print(0)
    elif lis[0]<lis[1] and lis[1]<lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)
        
# } Driver Code Ends
