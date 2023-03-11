#!/usr/bin/python3
if '__name__' == '__main__':
    import sys.argv
counter = len(argv)
i = 0
if counter == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(counter))
    while counter > 0:
        print("{}:{}".format(i + 1, argv[i]))
        i = i + 1
