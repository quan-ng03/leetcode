def countBits1(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # Initial thought is to traverse through the numbers from 0 to n and for each value, count the number of 1s in its binary representation. Here we have
    # the solution with O(n log n) time complexity and O(n) space complexity.

    binary_list = []
    for i in range(n + 1):
        counter = 0
        while i > 0:
            bit = i % 2
            if bit == 1:
                counter += 1
            i //= 2
        binary_list.append(counter)
    return binary_list


def countBits2(n):
    # We can do better than this with O(n) time complexity and O(n) space complexity. The idea is to use the previous results to calculate the current result.
    # For example, if we have the result for 5, we can use it to calculate the result for 6. The result for 6 is the result for 5 plus 1 if 6 is odd, or the same as
    # the result for 6 divided by 2 if 6 is even. This is because the binary representation of 6 is the same as the binary representation of 3 with an additional 1
    # at the end. The same logic applies to all numbers. The result for 7 is the result for 3 plus 1, and the result for 8 is the result for 4. This is because the
    # binary representation of 8 is the same as the binary representation of 4 with an additional 0 at the end. This is the optimized solution with O(n) time complexity
    # and O(n) space complexity.
    binary_list = [0] * (n + 1)
    for i in range(1, n + 1):
        binary_list[i] = binary_list[i // 2] + i % 2
    return binary_list
