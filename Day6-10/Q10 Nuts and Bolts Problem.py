#User function Template for python3
class Solution:

    def matchPairs(self,nuts, bolts, n):
        nuts.sort()
        bolts.sort()
        ans = []
        for i in range(n):
            if nuts[i]== bolts[i]:
                ans.append(nuts[i])
                
        return ans
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
