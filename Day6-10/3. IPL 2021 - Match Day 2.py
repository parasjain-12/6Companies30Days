#Question Link : https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        
        lis = []
        ans = []
        n = len(arr)
        for i in range(k):
            if len(lis)==0:
                lis.append(arr[i])
            elif arr[i] > lis[-1]:
                while len(lis)>0 and  arr[i] > lis[-1]:
                    lis.pop()
                lis.append(arr[i])

            else:
                lis.append(arr[i])

        ans.append(lis[0])

        i = 0
        for j in range(k,n):
            if arr[i] == lis[0]:
                lis.pop(0)
            i+=1
            if len(lis)==0:
                lis.append(arr[j])
            elif arr[j] > lis[-1]:
                while len(lis)>0 and  arr[j] > lis[-1]:
                    lis.pop()
                lis.append(arr[j])

            elif arr[j] < lis[-1]:
                lis.append(arr[j])

            ans.append(lis[0])
        
        return ans
