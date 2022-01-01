#Your task is to complete this function
#Function should return complete string

def encode(s):
    temp = [s[0],1]
    newS= ''
    prev = s[0]
    for i in range(1,len(s)):
        if s[i] == prev:
            temp[1] += 1
            prev = s[i]
        else:
            newS += str(temp[0])+ str(temp[1])
            temp = [s[i],1]
            prev = s[i]
        
            
    newS += str(temp[0])+ str(temp[1])
    return newS
    
    # Code here

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends
