#User function Template for python3
import string
class Solution:
    def colName(self,n):
        alphabet_string = list(string.ascii_uppercase)
        if n<=26:
            return str(alphabet_string[n-1])
        temp = []
        char = ''
        while n>0:
            rem = n%26
            if rem != 0:
                n = n//26
                temp.append(rem)
            else:
                n = n//26 - 1
                temp.append(26)
                
        temp = temp[::-1]
        for i in range(len(temp)):
            char += alphabet_string[temp[i]-1]
            
        return char

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends
