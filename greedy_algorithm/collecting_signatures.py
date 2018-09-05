def min_segment():
    segment_pairs = {}
    # read file input
    with open("./3_4_covering_segments.in") as f:
        line_num = 0
        for line in f:
            line_num += 1
            # read the first item for the n of items and weight
            if line_num == 1:
                num_item = int(line)
            else:
                # read input
                if line is not None:
                    items = line.split()
                    if len(items) < 2:
                        break
                    key = int(items[0])
                    segment_pairs[key] = int(items[1])

    # let pairs be sorted segments
    pairs = []
    for key in (sorted(segment_pairs)):
        pairs.append([key, segment_pairs[key]])

    # let points by number of reduced segments to cover all segments
    points = []

    # let index by index of increment to move from left item to n
    # initialize at zero
    index = 0
    # while n items > index
    while index < len(pairs):
        # split left and right of segment
        l, r = pairs[index][0], pairs[index][1]
        # append segment to points
        points.append(r)
        # move to next item by incrementing index by 1
        index += 1

        # while there are remaining item && current.left <= last.right
        # we don't add point to segment by the inner loop and increment index by 1
        while index < len(pairs) and pairs[index][0] <= points[len(points)-1]:

            # optional to replace last right if current right is smaller than last right
            # questionable to me
            # but I need it to pass the programming challenge
            if pairs[index][1] < r:  # this will fix the issue of (2,3) within (1,4)
                points[len(points) - 1] = pairs[index][1]         # which is to update the last point in array

            index += 1

    return len(points)

if __name__ == '__main__':
    """
    Algorithmic Design and Techniques
    Solution to
    Programming Challenge 3-4: Collecting Signatures
    """
    print("total segments needed is %s" % min_segment())
