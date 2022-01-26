from sortedcontainers import SortedList

class Solution:
    def recoverArray(self, n, sums):
        minn = -min(sums)
        sums = SortedList([minn + s for s in sums])
        arr = [0]
        sums.remove(0)
        ans = []
        for _ in range(n):
            c = sums[0]
            ans.append(c)
            for s in list(arr):
                sums.remove(c + s)
                arr.append(c + s)

        for i in range(2 ** n):
            if minn == sum(ans[w] for w in range(n) if i & (1 << w)):
                for w in range(n):
                    if i & (1 << w):
                        ans[w] = -ans[w]
                return ans
