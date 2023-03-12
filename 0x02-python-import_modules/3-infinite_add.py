#!/usr/bin/python3
if __name__ == "__main__":
    import sys
counter = len(sys.argv) - 1
sum = 0
i = 0
while counter > 0:
    sum = sum + int(sys.argv[i + 1])
    i++
    counter--
print("{}".format(sum))
