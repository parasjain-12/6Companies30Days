#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        temp = arr[0]
        start = 0
        i = 1
        while i<=n:
            while temp>s and start<i-1:
                temp = temp - arr[start]
                start+=1
                
            if temp == s:
                return [start+1,i]
            if i<n:
                temp += arr[i]
                
            i+=1
        return [-1]
       #Write your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
