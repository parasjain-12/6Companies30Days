#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,st):
        # Code here
        neg= False
        if st[0]=='-':
            neg = True
            st = st[1:]
        
        ans = []
        for i in range(len(st)-1,-1,-1):
            if st[i] < '0' or st[i] > '9':
                return -1
                
            temp = ord(st[i]) - 48
            ans.append(temp)
            

        inter =0
        n = len(ans)
        k = 0
        for i in range(len(ans)):
            # print(ans[i])
            inter+= ans[i]*(10**k)
            k+=1
            
        if neg == True:
            inter = inter*(-1)
            
        return inter

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends
