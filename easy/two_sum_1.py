

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
