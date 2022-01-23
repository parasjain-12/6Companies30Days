class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        lenth=len(grid)
        zeros=[0]*lenth
        for i in range(lenth):
            row=grid[i]
            for j in range(lenth):
                if row[-j-1]==0:
                    zeros[i]=j+1
                else:
                    break
        
        
        count=0
        
        for i in range(lenth):
            print(zeros)
            if zeros[i]<lenth-1-i:
                
                did=0
                for next in range(lenth-i-1):
                    if zeros[i+next+1]>=lenth-1-i:
                        did=1
                        k=i+next+1
                        while k - i >0:
                            count+=1
                            zeros[k],zeros[k-1] =zeros[k-1],zeros[k]
                            k-=1
                        break
                        
                if did==0:
                    return -1
        return count
