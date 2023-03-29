#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i <= x:
            print("{:d}".format(my_list[x]))
            i++     
    except (IndexError,TypeError):
        pass
