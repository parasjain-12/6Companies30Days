class Solution:        
    def winnerOfGame(self, colors: str) -> bool:
        alice=0
        bob =0
        for i in range(1,len(colors)-1):
            if colors[i]=="A":
                if colors[i-1]=="A" and colors[i+1]=="A":
                    alice+=1
            else:
                if colors[i-1]=="B" and colors[i+1]=="B":
                    bob+=1
        return alice>bob
