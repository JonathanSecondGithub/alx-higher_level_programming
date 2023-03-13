#!/usr/bin/python3
def print_list_integer(my_list=[]):
    counter = len(my_list)
    i = 0
    while counter > 0:
        print("{}".format(my_list[i]))
        counter--
        i++
