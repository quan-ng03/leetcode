

"""
    Same logic as two sums. add them in the dict and if it exist return true, else return false
"""

def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        if len(nums) == 1:
            return False
        for num in nums:
            if num in dict:
                 return True
            else:
                 dict[num] = 1
        return False