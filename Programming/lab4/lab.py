"""6.009 Lab 4 -- Tent Packing"""

# NO IMPORTS ALLOWED!


# Example bag_list entries:
#      vertical 3x1 bag: { (0,0), (1,0), (2,0) }
#      horizontal 1x3 bag: { (0,0), (0,1), (0,2) }
#      square bag: { (0,0), (0,1), (1,0), (1,1) }
#      L-shaped bag: { (0,0), (1,0), (1,1) }
#      C-shaped bag: { (0,0), (0,1), (1,0), (2,0), (2,1) }
#      reverse-C-shaped bag: { (0,0), (0,1), (1,1), (2,0), (2,1) }


def pack(tent_size, missing_squares, bag_list, max_vacancy):
    """
    Pack a tent with different sleeping bag shapes leaving up to max_vacancy squares open
    :param tent_size: (rows, cols) for tent grid
    :param missing_squares: set of (r, c) tuples giving location of rocks
    :param bag_list: list of sets, each describing a sleeping bag shape
    Each set contains (r, c) tuples enumerating contiguous grid
    squares occupied by the bag, coords are relative to the upper-
    left corner of the bag.  You can assume every bag occupies
    at least the grid (0,0).
    :param max_vacancy: maximum number of non-rock locations which can be unoccupied
    :return:  None if no packing can be found; otherwise a list giving the
    placement and type for each placed bag expressed as a dictionary
    with keys
        "anchor": (r, c) for upper-left corner of bag
        "shape": index of bag on bag list
    """
    pass #TODO implementation



bag_list = [
    {(0, 0), (1, 0), (2, 0)},  # vertical 3x1 bag
    {(0, 0), (0, 1), (0, 2)},  # horizontal 1x3 bag
    {(0, 0), (0, 1), (1, 0), (1, 1)},  # square bag
    {(0, 0), (1, 0), (1, 1)},  # L-shaped bag
    {(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)},  # C-shaped bag
    {(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)},  # reverse C-shaped bag
]


if __name__ == '__main__':
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    pass
