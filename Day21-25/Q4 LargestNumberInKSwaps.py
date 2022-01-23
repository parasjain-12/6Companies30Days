#User function Template for python3

class Solution:
    def swap(self,string, i, j):
            
     
        return (string[:i] + string[j] +
                string[i + 1:j] +
                string[i] + string[j + 1:])
     
    def findMaximum(self,string, k, maxm):
         
        if k == 0:
            return
     
        n = len(string)
     
        for i in range(n - 1):
     
            for j in range(i + 1, n):
                if string[i] < string[j]:
     
                    string = self.swap(string, i, j)
                    if string > maxm[0]:
                        maxm[0] = string
     
                    self.findMaximum(string, k - 1, maxm)
     
                    string = self.swap(string, i, j)
    def findMaximumNum(self,s,k):
        maxm = [s]
        self.findMaximum(s,k,maxm)
        return maxm[0]
        #code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob=Solution()
        print(ob.findMaximumNum(s,k))

# } Driver Code Ends
