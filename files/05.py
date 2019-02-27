
# read in the file
# split into list
# traverse the list

def hop_counter():

    file = open('05.txt').read()
    hop_list = [int(number) for number in file.split()]

    i = 0
    hop_count = 0

    while i >= 0 and i < len(hop_list):
        hop_count += 1
        hop_value = hop_list[i]
        hop_list[i] = hop_value + 1
        i += hop_value

    return hop_count


def hop_counter_three():

    file = open('05.txt').read()
    hop_list = [int(number) for number in file.split()]

    i = 0
    hop_count = 0

    while i >= 0 and i < len(hop_list):
        hop_count += 1
        hop_value = hop_list[i]
        if hop_value >= 3:
            hop_list[i] = hop_value - 1
        else:
            hop_list[i] = hop_value + 1
        i += hop_value

    return hop_count
