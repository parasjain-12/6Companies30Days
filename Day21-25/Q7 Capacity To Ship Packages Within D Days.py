class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
            left = max(weights)
            right = sum(weights)
            while left < right:
                mid = left + (right - left) // 2
                if self.condition(mid, weights) <= D:
                    right = mid
                else:
                    left = mid+1
            return left

    def condition(self, k, weights):
            d = 0
            cur_weight = 0
            for weight in weights:
                if cur_weight + weight == k:
                    d += 1
                    cur_weight = 0
                elif cur_weight + weight > k:
                    d += 1
                    cur_weight = weight
                else:
                    cur_weight += weight
            return d+1 if cur_weight > 0 else d
