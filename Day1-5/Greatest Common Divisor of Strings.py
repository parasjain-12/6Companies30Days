class Solution:
    
    def gcd(self,a,b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        le = self.gcd(len(str1),len(str2))
        estimate = str1[:le]
        if estimate*(len(str1)//(len(estimate))) == str1 and estimate*(len(str2)//len(estimate)) == str2:
            return estimate
        return ''
        
