https://www.geeksforgeeks.org/problems/special-series-sum0903/1

class Solution:
    def sumOfTheSeries (self, n):
        sum=0
        series=0
        for i in range(1,n+1):
            sum=sum+i
            series=series+sum
        return series
