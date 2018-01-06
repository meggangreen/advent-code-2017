""" Day 2 challenge 1: determine the checksum.

    Given a spreadsheet of values, subtract the smallest from the largest of
    each row, then add differences. The puzzle input is in 02-1.txt.

"""

checksum = 0

with open("02-1.txt") as puzzle:
    for line in puzzle:
        vals = line.split()
        checksum = checksum + (max(vals) - min(vals))

print checksum

    # with open file
    # for each line
    #   find the min and max
    #   subtract
    #   add difference to checksum
    # return checksum
