#User function Template for python3

class Solution:
    
    def getParent(self,root):
        if root == None:
            return 
        d = {}
        que = []
        que.append(root)
        while que:
            ele = que.pop(0)
            if ele.left:
                d[ele.left.data] = ele
                que.append(ele.left)
            if ele.right:
                d[ele.right.data] = ele
                que.append(ele.right)
        return d
        
    def search(self,root,target):
        if root == None:
            return 
        if root.data == target:
            return root
        
        check = self.search(root.left,target)
        if check != None :
            return check
        
        return self.search(root.right,target)
        
    def minTime(self, root,target):
        dic = self.getParent(root)
        targetNode = self.search(root,target)
        
        visited = set()
        time = 0
        que = []
        que.append(targetNode)
        # print("test",dic,que)
        while que:
            k = len(que)
            # print(que)
            while k>0:
                k-=1
                ele = que.pop(0)
                # print(ele,ele.data)
                visited.add(ele.data)

                        
                try:
                    if dic[ele.data] and dic[ele.data].data not in visited:
                        que.append(dic[ele.data])
                except:
                    pass
                if ele.left and ele.left.data not in visited:
                    que.append(ele.left)
                if ele.right and ele.right.data not in visited:
                    que.append(ele.right)
                    
            time += 1
        return time-1
        
        
       


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends
