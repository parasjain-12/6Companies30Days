class Solution:
    def minEatingSpeed(self, piles, H):
        beg, end = 0, max(piles)
        while beg + 1 < end:
            mid = (beg + end)//2
            if sum(ceil(i/mid) for i in piles) > H:
                beg = mid
            else:
                end = mid
                
        return end
