"""
First check if length of s is odd, if it is return False
Goes into the loop and for every found open bracket, insert the corresponding closing bracket in the first index of the storage list
If it finds a closing bracket, first check if storage is empty, then check if the first index of the storage list is the same as the
closing bracket, if it is, pop it from the list.
By the end of s, return false if storage is not empty, else return true.
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    storage = []
    dict = {"(": ")", "{": "}", "[": "]"}
    if len(s) % 2 != 0:
        return False
    for i in range(len(s)):
        if s[i] in dict.keys():
            storage.insert(0, dict[s[i]])
        elif s[i] in dict.values():
            if len(storage) == 0:
                return False
            elif s[i] == storage[0]:
                storage.pop(0)
            else:
                return False
        else:
            return False

    if len(storage) == 0:
        return True
    else:
        return False
