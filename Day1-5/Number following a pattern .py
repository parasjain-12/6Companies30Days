#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,s):
        arr = [0]*(len(s)+1)
        
        var = 1
        li = s.split('I')
        inde = []
        for i in range(len(s)):
            if s[i] == 'I':
                inde.append(i)
                
        inde.append(i+1)
        
        st = 0
        end = len(s)
        while len(inde)>0:
            index = inde.pop(0)
            while index>=st  and index<=end:
                if arr[index] == 0:
                    arr[index] = var
                    var+=1
                    index -= 1
                else:
                    break
                
        t1=  ''.join(str(x) for x in arr)
        return int(t1)
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends
