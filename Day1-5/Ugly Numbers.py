#User function Template for python3
class Solution:
    def getNthUglyNo(self,n):
        li = [1]
        twoP = 0
        threeP = 0
        fiveP = 0
        # code here
        while len(li)<n:
            two_V = li[twoP]*2
            three_V = li[threeP]*3
            five_V = li[fiveP]*5
            mi = min(three_V,two_V,five_V)
            
            if mi == three_V:
                threeP+=1
            if mi == five_V:
                fiveP+=1
            if mi == two_V:
                twoP+=1
                
            li.append(mi)
            
        return li[-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends
