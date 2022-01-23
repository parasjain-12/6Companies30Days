import math
MAX_DIGITS = 6

def getValue(Str, i, m):
   
    if(i + m > len(Str)):
        return -1
       
    value = 0
 
    for j in range(m):
        c = (ord(Str[i + j]) -
             ord('0'))
        if(c < 0 or c > 9):
            return -1
        value = value * 10 + c
    return value

def missingNumber(Str):

    for m in range(1, MAX_DIGITS + 1):
 
        n = getValue(Str, 0, m)
        if(n == -1):
            break

        missingNo = -1
        fail = False
        i = m
        while(i != len(Str)):
            if((missingNo == -1) and
               (getValue(Str, i, 1 +
                int(math.log10(n + 2))) ==
                               n + 2)):
                missingNo = n + 1
                n += 2
 
            elif((getValue(Str, i, 1 +
                  int(math.log10(n + 1))) ==
                                 n + 1)):
                n += 1
            else:
                fail = True
                break
            i += 1 + int(math.log10(n))
 
        if(not fail):
            return missingNo
           

    return -1


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        string = input().strip()
        print(missingNumber(string))
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
