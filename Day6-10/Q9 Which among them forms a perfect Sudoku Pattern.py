# Question Link : https://practice.geeksforgeeks.org/problems/is-sudoku-valid4820/1/

class Solution:
    def isValid(self, mat):
        # print(mat)
        d = set()
        row = len(mat)
        col = len(mat[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j]>0:
                    box = (i//3)*3 + (j//3)
                    s1 = 'row' + str(i) + str(mat[i][j])
                    s2 = 'col' + str(j) + str(mat[i][j])
                    s3 = 'box' + str(box) + str(mat[i][j])
                    if s1 in d or s2 in d or s3 in d:
                        return 0
                    else:
                        d.add(s1)
                        d.add(s2)
                        d.add(s3)
                                
        return 1
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends
