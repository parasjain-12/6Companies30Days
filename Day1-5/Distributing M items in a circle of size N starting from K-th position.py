#Interview Bit Question Link: https://www.interviewbit.com/problems/distribute-in-circle/

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A>B:
            A = A%B
        if C>B:
            C = C%B
        ans = C+A-1
        if ans>B:
            ans = ans%B

        return ans
