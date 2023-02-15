
def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            # i is a list of indices
            for i in index_all(search_list[index], item):
                index_list.append([index]+i) # This is concatenating two lists.
    return index_list


if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    #
    #  index=0
    #  value=[[1, 2, 3], 2, [1, 3]]
    #  index=0
    #  value=[1, 2, 3]
    #  [1]
    #  [0] + [1] = [0 + 1
    #
    # example = [
    #   0          [
    #      0          [
    #         0          1,
    #         1          2,   [0,0,1]
    #         2          3
    #                 ],
    #      1          2,      [0,1]
    #      2          [
    #          0         1,
    #          1         3
    #                 ]
    #              ],
    #   1          [
    #       0         1,
    #       1         2,     [1,1]
    #       2         3
    #              ],
    #   2          2         2
    #           ]
    # should find:
    print(f'       {index_all(example, 2)}')
    print('EXPECT [[0, 0, 1], [0,1], [1,1], 2]')
