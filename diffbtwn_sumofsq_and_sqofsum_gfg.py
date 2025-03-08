#https://www.geeksforgeeks.org/problems/squares-difference0939/1

class Solution:
    def squaresDiff (self, N):
        import math
        series=0
        add=0
        for i in range(1,N+1):
            sum=pow(i,2)
            series=series+sum
            add=add+i
            sq_series=pow(add,2)
        return(abs(series-sq_series))
