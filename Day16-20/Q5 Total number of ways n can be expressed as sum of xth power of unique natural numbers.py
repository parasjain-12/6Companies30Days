#User function Template for python3
class Solution:
    def checkRecursion(self,num,rem_num,cur_num,n,ans=0):
            if rem_num==0:
                ans+=1
                
            r = int(num**(1/n))
            for i in range(cur_num+1,r+1):
                temp = rem_num - int(i**n)
                if temp>=0:
                    ans+= self.checkRecursion(num,temp,i,n,0)
            return ans
    def numOfWays(self, n, x):
        
        t1 = self.checkRecursion(n,n,0,x,0)
        # code here
        return t1%1000000007


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,x = input().split()
        n=int(n)
        x=int(x)
        ob = Solution();
        print(ob.numOfWays(n, x))

# } Driver Code Ends
