"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

:type nums: List[int]
:type target: int
:rtype: List[int]

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# This one consists of two loops where it checks all the possible options.
# The time complexity for this is O(n^2)
def firstApproach(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return 0

# This one has only one loop where it uses the dictionary to store the "wrong answers" which uses subtraction to determine. If the answer is in the dictionary, then that's the answer.
# The time complexity for this is O(n).
def secondApproach(nums, target):
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict:
            return [i, dict[target-nums[i]]]
        else:
            dict[nums[i]]= i
    return 0

def main():
    print(firstApproach([3,2,4], 6))
    print(secondApproach([3,2,4], 6))

main()