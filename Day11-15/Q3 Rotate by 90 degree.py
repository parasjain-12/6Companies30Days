#User function Template for python3

def rotate(mat): 
    row = len(mat)
    col = len(mat[0])
    
    for i in range(row):
        for j in range(i+1,col):
            # print(i,j)
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
            
    for i in range(row//2):
        temp = mat[i]
        mat[i] = mat[row-1-i]
        mat[row-1-i] = temp
    
    return mat
    #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N=int(input())
        arr=[int(x) for x in input().split()]
        matrix=[]

        for i in range(0,N*N,N):
            matrix.append(arr[i:i+N])

        rotate(matrix)
        for i in range(N): 
            for j in range(N): 
                print(matrix[i][j], end =' ') 
            print() 
        

# } Driver Code Ends
