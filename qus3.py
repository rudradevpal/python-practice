"""
Qus 3. Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x
and y coordinates of two points: the left top corner and the right bottom corner of the rectangle.
Two rectangles sharing a side are considered overlapping.
(L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).

Note: It may be assumed that the rectangles are parallel to the coordinate axis.
"""


# Method 1
def do_rectangles_overlap(L1, R1, L2, R2):
    # Extract coordinates for Rectangle 1
    x1_1, y1_1 = L1
    x1_2, y1_2 = R1

    # Extract coordinates for Rectangle 2
    x2_1, y2_1 = L2
    x2_2, y2_2 = R2

    # Check if one rectangle is to the left of the other
    if x1_2 < x2_1 or x2_2 < x1_1:
        return False

    # Check if one rectangle is above the other
    if y1_2 < y2_1 or y2_2 < y1_1:
        return False

    return True


# Example usage
L1 = (1, 5)
R1 = (4, 2)
L2 = (2, 6)
R2 = (5, 3)

print(do_rectangles_overlap(L1, R1, L2, R2))  # Output: True
