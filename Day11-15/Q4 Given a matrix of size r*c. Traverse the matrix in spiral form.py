#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,mat, r, c): 
        # code here 
        row_i = 0
        col_i= 0
        row_end = r
        col_end = c
        ans = []
        var = 0
        while var<r*c:
            #Adding in First Row
            for j in range(col_i,col_end):
                ans.append(mat[row_i][j])
                var+=1
            row_i += 1
            
            #Addding in last col
            if var>=r*c:
                break
            for i in range(row_i,row_end):
                ans.append(mat[i][col_end-1])
                var += 1

                
            col_end -= 1
            if var>=r*c:
                break
            #Adding in last row
            for j in range(col_end -1,col_i-1,-1):
                ans.append(mat[row_end-1][j])
                var+=1
                
            row_end -= 1
            if var>=r*c:
                break
                
            #Adding in First col
            for i in range(row_end-1,row_i-1,-1):
                ans.append(mat[i][col_i])
                var+=1
                
            col_i+=1
            
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
