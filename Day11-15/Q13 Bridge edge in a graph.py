#User function Template for python3

class Solution:
    
    def dfs(self,node,parent,vis,time,low,adj,var,c,d,ans):
        vis[node] = 1
        var+=1
        low[node] = var
        time[node] = var
        for i in adj[node]:
            if i == parent:
                continue
            if vis[i] == 0:
                self.dfs(i,node,vis,time,low,adj,var,c,d,ans)
                low[node] = min(low[node],low[i])
                
                if low[i]>time[node]:
                    if i == c and node == d or i == d and node == c:
                        ans.append([c,d])
            else:
                low[node] = min(low[node],time[i])
                
                
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, n, adj, c, d):
        
        visited = [0]*n
        low = [-1]*n
        time = [-1]*n
        var = 0
        ans = []
        for i in range(n):
            self.dfs(i,-1,visited,time,low,adj,var,c,d,ans)
            if len(ans)>0:
                return 1
        # code here
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends
