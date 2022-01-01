#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        li = []
        for i in range(n):
            li.append([words[i],i])
            
            
        for i in range(n):
            li[i][0] = ''.join(sorted(li[i][0]))
            
            
        li = sorted(li, key = lambda k : k[0])
        
        ans = []
        temp = []
        temp.append(words[li[0][1]])
        for i in range(1,n):
            if li[i-1][0] == li[i][0]:
                ind = li[i][1]
                temp.append(words[ind])
            else:
                ans.append(temp)
                temp = []
                ind = li[i][1]
                temp.append(words[ind])
                
        ans.append(temp)
        
        return ans

#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
