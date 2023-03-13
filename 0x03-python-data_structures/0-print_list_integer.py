#!/usr/bin/python3
def print_list_integer(my_list=[]):
    counter = len(my_list)
    i = 0
    while counter > 0:
        print("{}".format(int(my_list[i])))
        counter -= 1
        i += 1
