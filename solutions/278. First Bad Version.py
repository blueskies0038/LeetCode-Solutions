# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        start = 1
        end = n
        while start + 1 < end and start > 0:
            mid = (end + start)//2 
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        return end