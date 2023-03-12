#!/usr/bin/python3
if __name__ == '__main__':
    import sys.argv
counter = len(argv)
i = 0
if counter == 0:
    print("0 arguments.")
elif counter == 1:
    print("1 argument:")
    print("{}: {}".format(counter, argv[counter]))
else: 
    print("{} arguments:".format(counter))
    while counter > 0:
        print("{}: {}".format(i + 1, argv[i]))
        i = i + 1
        counter = counter - 1
