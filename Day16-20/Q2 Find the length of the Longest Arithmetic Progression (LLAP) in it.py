#User function Template for python3

class Solution:
    def lengthOfLongestAP(self, arr, n):
        
        if n == 1 or n == 2:
            return n
            
        mat = [[0 for i in range(n)] for i in range(n)]
        maximum = 2
        for i in range(n-1):
            mat[i][n-1] = 2
            
        j =len(arr)-2
        while j>=0 :
            i = j-1
            k = j+1
            while i>=0 and k<n and i<j<k:
                first = arr[i]
                second = arr[j]
                third = arr[k]
                temp = first+third
        #         print(temp,2*second,i,j,k)
                if temp == 2*second:
                    mat[i][j] = mat[j][k]+1
                    maximum = max(maximum,mat[i][j])
                    i-=1
                    k+=1
                elif temp < 2*second:
                    k+=1
                else:
                    mat[i][j] = 2
                    i-=1
            while i>=0:
                mat[i][j] = 2
                i-=1
            j-=1

        # code here
        return maximum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.lengthOfLongestAP(A, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
