

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, arr, N):
        
        
        st = []
        for i in range(len(arr)-1,-1,-1):
            # print(arr[i])
            if len(st)== 0:
                st.append(arr[i])
                
            elif arr[i]>= st[-1]:
                st.append(arr[i])
        #Code here

        return st[::-1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
