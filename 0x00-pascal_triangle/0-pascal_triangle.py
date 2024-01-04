#!/usr/bin/python3
"""Pascal's Triangle
"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    pasTran = []

    for i in range(n):
        # First element
        my_List = [1]
        if i == 0:
            pasTran.append(my_List)
            continue

        k = i - 1
        for j in range(len(pasTran[k])):
            if j + 1 == len(pasTran[k]):
                # Last element
                my_List.append(1)
                break
            # Add two previous values to get current next value
            nextVal = pasTran[k][j] + pasTran[k][j + 1]
            my_List.append(nextVal)
        pasTran.append(my_List)

    return pasTran
