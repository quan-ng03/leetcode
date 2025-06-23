"""
This problem is similar to building a pyramid given the height.
Given the first number "num" and the number of times"t" following the operation,
X can be calculated by multiplying t by 2 and add "num".
"""


def theMaximumAchievableX(num, t):
    if t < 1:
        return num
    return num + 2 * t
