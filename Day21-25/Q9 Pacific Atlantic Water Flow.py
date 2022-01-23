class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        
        #get adjacent nodes, i.e. there is an edge
        def adjacent(r, c):
            for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= i < R and 0 <= j < C and matrix[r][c] <= matrix[i][j]:
                    yield (i, j)
        
        #Atlantic BFS
        que = collections.deque([])
        atlantic = [[0]*C for _ in range(R)]
        for r in range(R):
            que.append((r, C-1))
        for c in range(C-1):
            que.append((R-1, c))
        while que:
            r, c = que.popleft()
            atlantic[r][c] = 1
            for i, j in adjacent(r, c):
                if not atlantic[i][j]:
                    que.append((i, j))
        
        #Pacific BFS
        que = collections.deque([])
        pacific = [[0]*C for _ in range(R)]
        for r in range(R):
            que.append((r, 0))
        for c in range(1, C):
            que.append((0, c))
        while que:
            r, c = que.popleft()
            pacific[r][c] = 1
            for i, j in adjacent(r, c):
                if not pacific[i][j]:
                    que.append((i, j))
        
        #Find all nodes that can access both Oceans
        ans = []
        for r in range(R):
            for c in range(C):
                if atlantic[r][c] and pacific[r][c]:
                    ans.append([r, c])
        return ans        
