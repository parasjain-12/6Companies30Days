#User function Template for python3
class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        s = 0
        p = 1
        res = 0
        for e in range(len(arr)):
            p *= arr[e]
            while p>= k and s<e:
                p = p//arr[s]
                s+=1
            if p<k:
                le = e-s+1
                res += le
                
        return res
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
