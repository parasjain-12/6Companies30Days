#Brute Force

def countTotalSquare(n):
    ans = 0
    for i in range(n):
        ans += (n-i)*(n-i)
        
    return ans
  
  
  
#Using fromula sum of square of n natural number 
def countTotalSquare(n):
    return (n*(n+1)*(2*n+1))//6
