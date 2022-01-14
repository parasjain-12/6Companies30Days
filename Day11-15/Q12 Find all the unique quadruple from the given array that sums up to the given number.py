#Question Link : https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, arr: List[int], k: int) -> List[List[int]]:
        
        arr.sort()
        ans = []
        for i in range(len(arr)-3):
            for j in range(i+1,len(arr)-2):
                start = j+1
                end = len(arr)-1
                while start < end:
                    temp = arr[i] + arr[j] + arr[start] + arr[end]
                    if temp == k:
                        t1 = [arr[i],arr[j],arr[start],arr[end]]
                        t1.sort()
                        if t1 not in ans:
                            ans.append(t1)
                        start+=1
                        end-=1
                    elif temp > k:
                        end-=1
                    else:
                        start+=1
        # code here
        return ans
