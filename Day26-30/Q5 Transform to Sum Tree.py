#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def sumT(self,root):
        if root == None:
            return 0
        cur = root
        leftSum = self.sumT(cur.left)
        rightSum = self.sumT(cur.right) 
        if leftSum == 0 and rightSum == 0:
            temp = cur.data
            cur.data = 0
            return cur.data+temp
                
        else:
            temp = cur.data
            cur.data = leftSum + rightSum
            return cur.data+temp
            
    def toSumTree(self, root) :
        #code here
        self.sumT(root)
        return root
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
import sys
sys.setrecursionlimit(10**6)
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
    
# A utility function to print  
# inorder traversal of a Binary Tree  
def printInorder(Node) : 
    if (Node == None) : 
        return
    printInorder(Node.left)  
    print(Node.data, end = " ")  
    printInorder(Node.right)  
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        ob.toSumTree(root)
        printInorder(root)
        print()
# } Driver Code Ends
