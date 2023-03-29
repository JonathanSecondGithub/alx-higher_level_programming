#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i <= x:
            print(my_list[x])
            i++     
    except IndexError:
        pass
