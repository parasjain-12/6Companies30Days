#Time Complexity: O(n)

class Solution:
    def minSubArrayLen(self, t: int, arr: List[int]) -> int:
        
        
        left = 0
        right = 0
        ans = 10000000
        temp = 0

        while left<= right and right < len(arr)+1:
            if temp < t and right<len(arr):
                temp += arr[right]
                right +=1
            elif temp >= t:
                temp -= arr[left]
                ans = min(ans,right-left)
                left+=1
            else:
                break
                
        if ans == 10000000:
            return 0
        return ans
         
