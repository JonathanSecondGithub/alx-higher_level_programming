#!/usr/bin/python3
if __name__ == "__main__":
    import sys
counter = len(sys.argv) - 1
sum = 0
i = 1
while counter > 0:
    sum = sum + sys.argv[i]
    i++
    counter--
print("{}".format(sum))
