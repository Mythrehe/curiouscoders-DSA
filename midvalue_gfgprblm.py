#https://www.geeksforgeeks.org/problems/middle-of-three2926/1

class Solution:
    def middle(self, a, b, c):
        if(b>a and c<a or b<a and c>a):
            return a
        elif(a>b and c<b or a<b and c>b):
            return b
        else:
            return c
