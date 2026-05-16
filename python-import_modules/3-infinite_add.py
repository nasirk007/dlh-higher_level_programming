#!/usr/bin/python3
import sys

# execute the code if this file is a main or just like admin"
if __name__ == "__main__":
    # define what is argument and from where it will come from, user or system
    argument = sys.argv
    # store result of each addition after converting each argument into integer
    total = 0
    # indexing will start from 1 as sys.argv itself is first argument in list
    for i in range(1, len(sys.argv)):
        # sys.argv[i] will return value instead of integer
        total += int(sys.argv[i])
    print(total)
