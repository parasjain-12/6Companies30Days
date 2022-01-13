class Solution:
    def dfs(self,mat,i,j,row,col,count):
    #     print("Inside function",i,j,count)
        que = []
        mat[i][j]=2
        que.append([i,j])
        while que:
            # print(que)
            x = que.pop(0)
            i  = x[0]
            j = x[1]
            #TOP LEFT
            if i-1>=0 and j-1>=0 and mat[i-1][j-1]==1:
                count+=1
                mat[i-1][j-1] = 2
                que.append([i-1,j-1])
                
            #TOP mid
            if i-1>=0 and mat[i-1][j]==1:
                mat[i-1][j] = 2 
                count+=1
                que.append([i-1,j])
                
            #top Right
            if i-1>=0 and j+1<col and mat[i-1][j+1] == 1:
                count+=1
                mat[i-1][j+1]=2
                que.append([i-1,j+1])
                
            #left 
            if j-1>=0 and mat[i][j-1]==1:
                mat[i][j-1] =2
                count+=1
                que.append([i,j-1])
            
            #Right
            if j+1<col and mat[i][j+1] ==1:
    
                mat[i][j+1] =2
        #         print("ddd")
                count+=1
                que.append([i,j+1])
                
    
            #Bottom Left
        #     print("Bottom Left",i+1,row,j-1)
            if i+1 <row and j-1>=0 and mat[i+1][j-1] ==1:
                count+=1
                mat[i+1][j-1] =2            
                que.append([i+1,j-1])
    
    
            #Bottom mid
            if i+1 <row and  mat[i+1][j] ==1:
                mat[i+1][j] = 2
                count+=1
                que.append([i+1,j])
    
    
    
            #Bottom mid right
        #     print(i+1<=row)
            if i+1 <row and j+1<col and mat[i+1][j+1] ==1:
                mat[i+1][j+1] = 2
                count+=1
                que.append([i+1,j+1])
            
            
        return count

    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, mat):
       # print(mat)
        row = len(mat)
        col = len(mat[0])
        ans = []
        # print(col)
        count = 0
        
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    count = 1
        #             print(i,j)
                    ans.append(self.dfs(mat,i,j,row,col,1))
                    mat[i][j]=2
                    
        return max(ans)
        #Code here


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends
