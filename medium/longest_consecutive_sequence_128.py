from typing import List


def longestConsecutive(nums: List[int]) -> int:
    sorted_list = sorted(set(nums))
    count = 1
    longest = 1

    if len(nums) < 1:
        return 0
    for i in range(len(sorted_list) - 1):
        if sorted_list[i + 1] == sorted_list[i] + 1:
            count += 1
        else:
            longest = max(longest, count)
            count = 1
    longest = max(longest, count)
    return longest
