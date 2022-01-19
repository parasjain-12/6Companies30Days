#User function Template for python3

class Solution:
    def valid(self,n,op,cl,st,ans):
        # print(st,op,cl)
        if cl>op or op>n or cl>n: 
            return 
        if op == cl == n:
            ans.append(st)
            return 
        #option 1
        temp = st+ '('
        self.valid(n,op+1,cl,temp,ans)
        
        #option 2
        temp1 = st+')'
        self.valid(n,op,cl+1,temp1,ans)
    def AllParenthesis(self,n):
        ans = []
        self.valid(n,0,0,'',ans)
        return ans
        #code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends
