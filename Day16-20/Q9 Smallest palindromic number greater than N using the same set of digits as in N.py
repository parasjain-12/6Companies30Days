#User function Template for python3

class Solution:
    def sortAr(self,arr,start,end):
        temp = arr[start:end+1]
        # print("Given Array",arr,temp)
        temp.sort()
        k = 0
        for i in range(len(arr)):
            if start<=i<=end:
                arr[i] = temp[k]
                k+=1
                
        return arr
        
    
    def nextGreaterEle(self,sub):
        n = len(sub)
        for i in range(n-1,0,-1):
            if sub[i]>sub[i-1]:
                first = sub[i-1]
                mi = 1111111111
                index  = -11
                for j in range(i,n):
                    if sub[j]>first:
                        if sub[j]<mi:
                            mi = sub[j]
                            index = j
                #Swap
                sub[i-1],sub[index] = sub[index],sub[i-1]
                
                #Sort            
                arr = self.sortAr(sub,i,n)
                return arr
        return -1
        
    def nextPalin(self,N):
        n = len(N)
        if n<4:
            return -1
            
        arr = list(int(x) for x in N)
        mid = len(arr)//2
        ans = self.nextGreaterEle(arr[:mid])
        # print(ans)
        if ans == -1:
            return ans
        else:
            t1 = ''.join(str(x) for x in ans)
            lastPart = ans[::-1]
            if n %2 != 0:
                t1+= str(arr[mid])
            for i in range(len(lastPart)):
                t1+= str(lastPart[i])
                    
            return t1
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.nextPalin(s))
# } Driver Code Ends
