## Question Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, num: str) -> List[str]:
        
        arr = ['0','0','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        if len(num) == 0:
            return []
        if len(num)==1:
            return list(arr[int(num[0])])
        ch = num[0]#1
        res = num[1:]#24
        resList = self.letterCombinations(res)
        ans = []
        for i in range(len(arr[int(ch)])):
            for j in range(len(resList)):
                temp = resList[j]
                t2 =  list(arr[int(ch)])[i] + temp
                ans.append(t2)

        return ans
