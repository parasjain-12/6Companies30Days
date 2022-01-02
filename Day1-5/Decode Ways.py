#Solution ran fine in leetcode but giving TLE in GeeksForGeeks compiler
class Solution:
        
        
    def Count(self,a,n):
        arr = [0]*(n)
        i = 1
        arr[0] = 1
        while i < n:
            if a[i] != '0':
                arr[i] = arr[i-1]
            if a[i-1] == '1' or (a[i-1]=='2' and a[i] <= '6'):
                if i-2>0:
                    arr[i] += arr[i-2]
                else:
                    arr[i] += 1
            i+=1
            
        return arr[-1]
        
    def numDecodings(self, n):
	    if len(n) == 0 or (len(n) == 1 and n[0] =='0') or n[0] == '0':
	        return 0
	    return self.Count(n,len(n))
