#https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

class Solution:
    def sumOfSeries(self,n):
        import math
        series=0
        for i in range(1,n+1):
            sum=pow(i,3)
            series=series+sum
        return series
