class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        N = len(isConnected)
        visited = [False] * N

        conn = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if i != j:
                    if isConnected[i][j] == 1:
                        conn[i].append(j)

        def dfs(i):
            for j in conn[i]:
                if visited[j] == False:
                    visited[j] = True
                    dfs(j)

        nprov = 0
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                nprov += 1
                dfs(i)

        return nprov
        
