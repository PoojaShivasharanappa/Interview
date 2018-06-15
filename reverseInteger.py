class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        rev = 0
        if x < 0:
            x = x * -1
            negative = True
        while x>0:
            digit = x%10
            x = int(x/10)
            rev = rev*10+digit
            print(rev)
        if negative == True:
            rev = rev * -1
        if rev<-2147483648 or rev>2147483647:
            return 0
        return rev
