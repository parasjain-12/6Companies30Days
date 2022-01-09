class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        
        totalOrange = 0
        correctOrange = 0
        queue = []
        row = len(mat)
        col = len(mat[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j] >0:
                    totalOrange+=1
                    if mat[i][j] == 1:
                        correctOrange+=1
                    if mat[i][j] == 2:
                        queue.append([i,j])

        visited = [[0 for i in range(col)] for j in range(row)]
        cnt = 0
        rotten = totalOrange - correctOrange
        if correctOrange == 0:
            return 0

        while queue:

            # print("Queue",queue)
            t1 = 0
            k = len(queue)
            cnt += 1
            while k>0:

                ele = queue.pop(0)
                left = ele[0]
                right = ele[1]
                visited[left][right] =1
                k-=1

                #TOP element
                if left-1>=0:
                    if mat[left-1][right] == 1 and visited[left-1][right] == 0:
                        queue.append([left-1,right])
                        visited[left-1][right]=1
                        rotten+=1

                #Right Element
                if right+1<col:
                    if mat[left][right+1]==1 and visited[left][right+1]==0:
                        queue.append([left,right+1])
                        visited[left][right+1]=1
                        rotten+=1

                #bottom Element
                if left+1<row:
                    if mat[left+1][right] == 1 and visited[left+1][right] ==0:
                        queue.append([left+1,right])
                        visited[left+1][right] = 1
                        rotten+=1

                #left element
                if right -1 >=0:
                    if mat[left][right-1]==1 and visited[left][right-1] == 0:
                        queue.append([left,right-1])
                        visited[left][right-1] = 1
                        rotten+=1

        if rotten >= totalOrange:
            return cnt-1
        else:
            return -1
        
