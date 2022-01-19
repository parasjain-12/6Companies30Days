#User function Template for python3
import re

class Solution:

    def amendSentence(self, s):
        temp = ''
        flag = False
        for i in range(len(s)):
            if s[i].isupper():
                if len(temp)==0:
                    temp += s[i].lower()
                else:
                    temp+= ' '
                    temp += s[i].lower()
                
            else:
                temp += s[i]
                
        return temp
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.amendSentence(s))
        

# } Driver Code Ends
