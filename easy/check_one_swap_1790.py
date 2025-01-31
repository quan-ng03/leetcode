"""
"""

def areAlmostEqual(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        s1 = list(s1)
        s2 = list(s2)
        temp = ""
        for i in range(len(s1)):
            for j in range(i,len(s1)):
                temp = s1[i]
                s1[i] = s1[j]
                s1[j] = temp
                if str(s1) == str(s2):
                    return True
                else:
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp
        return False