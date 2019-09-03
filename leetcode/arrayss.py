class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        li = sorted((nums1 + nums2))
        s = len(li)
        if s % 2:
            return float(li[s // 2])
        else:
            return float((li[s // 2 - 1] + li[s // 2]) / 2)

a = Solution()
qw = [1,3]
qe = [2]
a.findMedianSortedArrays(qw,qe)