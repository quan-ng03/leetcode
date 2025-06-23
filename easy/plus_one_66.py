def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    """
        My first thought is to check if the last list element equals to 9 or not.
        If it doesn't, then I will plus one to that last element and return.
        If it does, then I will loop through the list from the end to the beginning.
        For each loop, add the value to a carry variable. After the loop, plus one.
        After that, use the map function to convert the int to list.
        The time complexity is O(n) where n is the number of digits in the list.
        The space complexity is O(n) if we consider the space used for the output list.
        """
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        number = 0
        multiplicity = 1
        for i in reversed(range(len(digits))):
            number = number + (digits[i] * multiplicity)
            multiplicity *= 10
        number += 1
        digits = list(map(int, str(number)))
        print(digits)
    return digits


def plusOneBetter(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    """
    For this solution, I optimized it by not using any built-in functions.
    This solution works by iterating through the list from right to left.
    If a digit is not 9, I increment it by one and return the list.
    If a digit is 9, I set it to 0 and continue to the next digit.
    If all digits are 9, I set the first digit to 1 and append 0 to the rest of the
    digits.
    The time complexity is O(n) and the space complexity is O(1). There's only one case
    where the space complexity is O(n) which is when all digits are 9.
    """
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
