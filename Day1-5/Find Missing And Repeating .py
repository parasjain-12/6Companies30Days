#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        miss = [0]*(len(arr))
        twice = 0
        for i in range(len(arr)):
            if miss[arr[i]-1] == 0:
                miss[arr[i]-1] = 1
            elif miss[arr[i]-1] == 1:
                twice = arr[i]
                

        miEle = 0
        for i in range(len(arr)):
            if miss[i] == 0:
                miEle = i+1
                break
                

        return [twice,miEle]
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
