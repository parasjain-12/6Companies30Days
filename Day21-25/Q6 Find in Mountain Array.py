# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
        
class Solution:
    def findInMountainArray(self, t: int, mountain_arr: 'MountainArray') -> int:
        if mountain_arr.get(0) == t:
            return 0
        low = 0
        high = mountain_arr.length()
        cur = (low+high)//2
        while cur != low and cur!=high:
            if mountain_arr.get(cur) > mountain_arr.get(cur+1) and mountain_arr.get(cur) > mountain_arr.get(cur-1):
                break
            if mountain_arr.get(cur) > mountain_arr.get(cur+1):
                high = cur
            else:
                low = cur
            cur = (low + high)//2
        mid = cur
        
        if mountain_arr.get(mid) == t:
            return mid
        low = 0
        high = mid
        cur = (low+high)//2
        while cur!=low and cur!= high:
            if mountain_arr.get(cur) < t:
                low = cur
            elif mountain_arr.get(cur) > t:
                high = cur
            else:
                return cur
            cur = (low+high)//2
        low = mid
        high = mountain_arr.length()
        cur = (low + high)//2
        while cur!=low and cur!= high:
            if mountain_arr.get(cur) > t:
                low = cur
            elif mountain_arr.get(cur) < t:
                high = cur
            else:
                return cur
            cur = (low+high)//2
        return -1
        
