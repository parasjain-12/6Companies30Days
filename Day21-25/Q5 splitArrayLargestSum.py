class Solution:
    def splitArray(self, nums, m):
            """
            :type nums: List[int]
            :type m: int
            :rtype: int
            """
            l, r = max(nums), sum(nums)

            def helper(target, m):
                sums = 0
                cnt = 0 
                for num in nums:
                    if num+sums>target:
                        cnt+=1
                        sums = 0
                    sums+=num
                return cnt>=m

            while l<=r:
                mid = (l+r)//2 
                if helper(mid, m):
                    l = mid+1
                else:
                    r = mid-1
            return l 
