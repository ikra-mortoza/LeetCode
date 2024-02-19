class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

s = Solution()
nums = [1,4,5,7,6,3,1]
print(s.containsDuplicate(nums))