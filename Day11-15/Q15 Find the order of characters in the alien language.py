#User function Template for python3

class Solution:
    
    def dfs(self,graph,visited,stack,K,v):
        visited[v] = 1
        for k in range(K):
            if graph[v][k] == 1 and visited[k] == 0:
                self.dfs(graph,visited,stack,K,k)
        stack.append(v)
        
        
        
    def findOrder(self,dic, N, K):
        graph = [[0 for i in range(K)] for j in range(K)]
        stack  = []
        
        for i in range(len(dic)-1):
            temp = dic[i]
            temp1 = dic[i+1]
            j = 0
            k = 0
            while j< len(temp) and k<len(temp1) and temp[j]==temp1[k] :
                j+=1
                k+=1
            if j<len(temp) and k<len(temp1):
                graph[ord(temp[j]) - ord('a')][ord(temp1[k]) - ord('a')]  = 1
            
            
        visited = [0]*K
        for i in range(K):
            if visited[i] == 0:
                self.dfs(graph,visited,stack,K,i)
                
        stack = stack[::-1]
        
        string = ''
        for i in range(len(stack)):
            string += chr(stack[i]+97)
            
        return string
        
    # code here
        # print(dic[0])


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
