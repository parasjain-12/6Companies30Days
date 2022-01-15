#User function Template for python3

class Solution:
    def solve(self,graph,order,visited,i):
        visited[i] = 1
        order[i] = 1
        for k in graph[i]:
            if  visited[k] == 0:
                conf = self.solve(graph,order,visited,k)
                if conf == True:
                    return True
            elif order[k] == 1:
                return 1
        order[i] = 0
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, n, graph):
        
        visited = [0]*n
        order = [0]*n
        for i in range(n):
            if visited[i] == 0:
                c = self.solve(graph,order,visited,i)
                if c == True:
                    return True
        return False
        
    def isPossible(self,n,li):
        
        graph = [[] for _ in range(n)]
        for i in range(len(li)):
            graph[li[i][1]].append(li[i][0])
            
        # print(graph)

        flag = self.isCyclic(n,graph)
        if flag:
            return False
                
        return True
        #code here
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
