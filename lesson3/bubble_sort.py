def bubble_sort(num_list, reverse=False):
    sorting_list = num_list.copy()
    n = len(sorting_list)
    if reverse:
        for i in range(n - 1):
            for j in range(n - i - 1):
                if sorting_list[j] < sorting_list[j + 1]:
                    sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]
    if not reverse:
        for i in range(n - 1):
            for j in range(n - i - 1):
                if sorting_list[j] > sorting_list[j + 1]:
                    sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]

    return sorting_list

if __name__ == "__main__":
    old_list = [4, 5, 7, 3, 2]
    new_list = bubble_sort(old_list)
    new_list_reverse = bubble_sort(old_list, True)
    print(old_list)
    print(new_list)
    print(new_list_reverse)
