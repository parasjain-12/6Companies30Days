#Question Link: https://leetcode.com/problems/longest-mountain-in-array/


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        incre = []
        decre = []
        n = len(arr)
        incre.append(0)
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                incre.append(1+incre[-1])
            else:
                incre.append(0)


        decre = [0]*n
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                decre[i] = 1 + decre[i+1]


        ans = 0
        for i in range(n):
            if incre[i] != 0 and decre[i]!= 0:
                ans = max(ans,1+incre[i]+decre[i])

        if ans >= 3:
            return ans
        return 0
