#User function Template for python3

class Solution:
    #Complete this function
    def power(self,x,y):
        MOD = 1000000007
        temp = 0
        if( y == 0):
            return 1
        temp = self.power(x, int(y / 2))
        if (y % 2 == 0):
            return temp * temp%MOD
        else:
            return x * temp * temp%MOD


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
