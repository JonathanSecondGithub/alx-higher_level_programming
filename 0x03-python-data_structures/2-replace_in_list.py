#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list2 = my_list
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        list2[idx] = element
    return (list2)
