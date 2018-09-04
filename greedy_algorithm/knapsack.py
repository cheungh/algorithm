def max_loot():
    # the number 𝑛 of items and the capacity 𝑊 of a knapsack
    capacity_num_item = 0
    capacity_weight = 0

    # let value_per_unit_dict by a dictionary to store value per unit
    # e.g {3 :[30, 10], 5 :[25, 5]}
    value_per_unit_dict = {}
    with open("3_2_loot.in") as f:
        # let line num be line number for file input
        line_num = 0
        for line in f:
            line_num += 1
            items = line.split()
            if items is None:
                continue

            # read the first item for the n of items and weight
            if line_num == 1:
                capacity_num_item = int(items[0])
                capacity_weight = int(items[1])
            else:
                # read item
                if len(items) < 2:
                    continue
                key = round(int(items[0]) / int(items[1]), 3);
                value_per_unit_dict[key] = [items[0], items[1]]

        # let sorted_loot_list by a reversed sorted list of loot item
        # e.g. order by the most valuable item on the left

        sorted_loot_list = []

        # reserve sort the dictionary and put into sorted_loot_list
        for key in reversed(sorted(value_per_unit_dict)):
            sorted_loot_list.append(value_per_unit_dict[key])

        # let loot total be the loot_total_amount
            loot_total_amount = 0

        for each in sorted_loot_list:

            # print(each)
            # get weight of the item
            item_weight = int(each[1])
            item_value = int(each[0])
            # check if the capacity is available

            if capacity_weight == 0:
                # done if we have no room for the knapsack
                break
            elif capacity_weight >= item_weight:
                # if there is room we will put item in knapsack
                loot_total_amount += item_value
                capacity_weight = capacity_weight - item_weight
            else:
                # capacity_weight remains the left over weight
                # therefore we need to see how much we can put in knapsack
                value_per_weight_unit = round(item_value / item_weight, 3)
                loot_total_amount += value_per_weight_unit * capacity_weight
                break

            # get value of the item
        return loot_total_amount


if __name__ == '__main__':
    """
    Algorithmic Design and Techniques
    solution to knapsack
    Programming Challenge 3-2: Maximum Value of the Loot
    
        
    algorithm
    1. read items to be loot
    2. sort items in reverse order
        most valuable on the left
    3. iterate from 0 to len(n)
    4. check if there is room to put item in knapsack
    5. Yes: (a) put item in knapsack, and 
            (b) subtract knapsack capacity from current item weight
    6. No:  (a) No room, break
            (b) some room, but not enough: put remaining capacity of current item into knapsack
    
    """
    print("total: is %.3f" % max_loot())
