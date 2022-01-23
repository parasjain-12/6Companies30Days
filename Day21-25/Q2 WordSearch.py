class Solution:
    def matchword(self,grid,word,i,j,row,col,x):
        if x == len(word):
            return 1
        
        if i<0 or i>= row or j<0 or j>=col:
            return 0
        
        if grid[i][j] == word[x] :

            temp = grid[i][j]
            grid[i][j] = '#'
            res = (self.matchword(grid,word,i-1,j,row,col,x+1) or 
                self.matchword(grid,word,i+1,j,row,col,x+1) or 
                self.matchword(grid,word,i,j+1,row,col,x+1) or
                self.matchword(grid,word,i,j-1,row,col,x+1) )
                
            # visited = temp
            grid[i][j] = temp
            return res
        else:
            return 0
        
    def isWordExist(self, grid, word):
        
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == word[0]:
                    if self.matchword(grid,word,i,j,row,col,0):
                        return 1 

        return 0
        #Code here

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n, m = map(int, input().split())
        board = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            board.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(board, word)
        if(ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
