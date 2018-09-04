def merge_sort(arr):
    if len(arr) < 2:
        return arr
    # divide into 2 half
    divider = len(arr) // 2
    arr1 = merge_sort(arr[0:divider])
    arr2 = merge_sort(arr[divider:])
    return merge(arr1, arr2)

def merge(arra, arrb):
    i = j = 0
    merge_list = []
    while i < len(arra) and j < len(arrb):
        if arra[i] < arrb[j]:
            merge_list.append(arra[i])
            i += 1
        else:
            merge_list.append(arrb[j])
            j += 1

    while i < len(arra):
        merge_list.append(arra[i])
        i += 1

    while j < len(arrb):
        merge_list.append(arrb[j])
        j += 1

    return merge_list


def max_advertise_revenue():
    # let total_revenue be total advertisement revenue
    total_revenue = 0

    # let ad_price_list be a list for ad amount price
    ad_price_list = []

    # let clicks_list be a list for click count
    clicks_list = []

    # read file input
    with open("./3_3_dot_product20180216.in") as f:
        line_num = 0
        for line in f:
            line_num += 1
            # read the first item for the n of items and weight
            if line_num == 1:
                num_item = int(line)
            else:
                # read ad revenue
                if line_num == 2:
                    items = line.split()
                    for item in items:
                        ad_price_list.append(int(item))

                # read clicks
                if line_num == 3:
                    items = line.split()
                    for item in items:
                        clicks_list.append(int(item))

    # merge sort
    clicks_list = merge_sort(clicks_list)

    # merge sort
    ad_price_list = merge_sort(ad_price_list)

    # loop through n items to add up revenue
    for index in range(0, len(clicks_list)):

        # add up advertisement revenue
        total_revenue += clicks_list[index] * ad_price_list[index]

    # return program output
    return total_revenue


if __name__ == '__main__':
    """
    Algorithmic Design and Techniques
    Solution to
    Programming Challenge 3-3: 
    Maximum Advertisement Revenue
    """
    print("total advertise revenue is %s" % max_advertise_revenue())
