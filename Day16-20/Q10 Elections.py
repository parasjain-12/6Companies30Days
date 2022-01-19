#User function Template for python3
from collections import Counter

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        dic = Counter(arr)# Your code here
        # return the name of the winning candidate and the votes he recieved
        ans = []
        ma = 0
        for k,v in dic.items():
            if v>= ma:
                ma = v
                
        
        for k,v in dic.items():
            # print(k,v)
            if v==ma:
                ans.append([k,v])

        ans= sorted(ans,key = lambda x:x[0])
    
        return ans[0][0],ans[0][1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends
