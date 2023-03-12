#!/usr/bin/python3
if __name__ == '__main__':
    import sys.argv
counter = len(argv)
i = 0
if counter == 0:
    print("{} arguments.".format(counter))
elif counter == 1:
    print("{} argument:".format(counter))
else:
    print("{} arguments:".format(counter))
while counter > 0:
    print("{}: {}".format(i + 1, argv[i + 1]))
    i = i + 1
    counter = counter - 1
