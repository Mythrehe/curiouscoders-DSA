#https://www.geeksforgeeks.org/problems/count-squares3649/1

class Solution:
    def countSquares(self, n):
        import math
        count=0
        for i in range(1,n):
            sq=pow(i,2)
            if(sq>=n):
               break
            else:
                count=count+1
        return count
