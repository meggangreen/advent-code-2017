""" Day 2 challenge 1: determine the divsum.

    Given a spreadsheet of values, find the only two numbers in each row where
    one evenly divides the other, then add the dividends. The puzzle input is in
    02-1.txt.

"""

divsum = 0

with open("02-1.txt") as puzzle:
    for line in puzzle:
        vals = line.split()
        vals = map(int, vals)  # change all to int
        dividend = None
        i = 0
        while i < len(vals):
            j = -1
            while j < len(vals) - 1:
                j += 1
                if j == i:
                    continue
                if vals[i] % vals[j] == 0:
                    dividend = vals[i] / vals[j]
                    break
                elif vals[j] % vals[i] == 0:
                    dividend = vals[j] / vals[i]
                    break
            if dividend is not None:
                divsum = divsum + dividend
                break
            i += 1

print divsum
