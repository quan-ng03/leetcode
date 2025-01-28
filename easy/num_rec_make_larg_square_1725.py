"""

"""

def countGoodRectangles(rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        
        dictionary = {}
        for i in range(len(rectangles)):
            if min(rectangles[i]) in dictionary.keys():
                dictionary[min(rectangles[i])] += 1
            else:
                dictionary[min(rectangles[i])] = 1
        return dictionary[max(dictionary)]