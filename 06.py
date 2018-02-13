def count_redistribution_cycles():
    # vars: count, len, configs, curr_config

    file = open('06.txt').read()
    banks = [int(number) for number in file.split(',')]

    configs = set()
    curr_config = banks
    count = -1

    while curr_config not in configs:
        count += 1
        configs.add(",".join([str(number) for number in curr_config]))
        max_blocks = max(curr_config)
        i = index(max(curr_config))

        while max_blocks > 0:
            if i + 1 == len(curr_config):
                i = -1
            i += 1
            curr_config[i] += 1
            max_blocks += -1

    return count