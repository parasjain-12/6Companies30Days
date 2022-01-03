#User function Template for python3

class Solution:
    def decodedString(self, s):

        newS = ''
        temp = ''
        st = []
        n = len(s)
        i=0
        while i<n:
            #Used the get the digit and append the digit in stack
            if s[i].isnumeric():
                t2 = ''
                while s[i].isnumeric():
                    t2 += s[i]
                    i+=1
        
                st.append(int(t2))
            if s[i] == '[':
                st.append('*')
                i+=1
            elif s[i] == ']':
                t1 = []
                while len(st)>0 and st[-1] != '*':
                    x = st.pop()
                    t1.append(x)
                st.pop()#Pop the '[' from the stack
                t1 = t1[::-1]#Reverse the string becz while popping the character are added in reverse order
                t1 = ''.join(t1)#Create a string from list of string 
                num = st.pop()#Pop the number from the stack 
                t1 = t1*int(num)# Multiply the number obtained in from previous step
                st.append(t1)
                i+=1
            else:
                st.append(s[i])
                i+=1
                
        return st[-1]
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends
