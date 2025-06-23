def deleteGreatestValue(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    """
        Initial constraint is grid cannot be empty, there's always at least 1 row and 1 column
        Brute force:
        - One loop to make changes on grid until it is empty
        - Another loop to perform operations on each row
        - After that second loop, store the max value among all rows and add to the result variable
        Time complexity is O(mn^2) and Space complexity is O(1)
        """
    result = 0
    while grid[0]:
        value = 0
        for i in range(len(grid)):
            if value < max(grid[i]):
                value = max(grid[i])
            grid[i].remove(max(grid[i]))
        result += value
        print(result, grid)
    return result


def deleteGreatestValueBetter(grid):
    """
    Optimized solution:
    -Sort the grid first
    -Swap the rows to columns and vice versa
    -Now each row will be the values being popped off each loop
    -Make a for loop that take the max value of each row and add to the result variable
    Time complexity is O(mn log(mn)) and Space complexity is O(mn)
    """
    for i in range(len(grid)):
        grid[i].sort()
    grid = list(map(list, zip(*grid)))
    result = 0
    for row in grid:
        result += max(row)
    return result
