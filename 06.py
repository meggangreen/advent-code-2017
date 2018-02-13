def count_redistribution_cycles():
    # vars: count, len, configs, curr_config

    file = open('06.txt').read()
    banks = [int(number) for number in file.split(',')]

    configs = set()
    curr_config = banks
    curr_config_s = ",".join([str(number) for number in curr_config])

    while curr_config_s not in configs:
        configs.add(curr_config_s)
        max_blocks = max(curr_config)
        i = curr_config.index(max(curr_config))
        curr_config[i] = 0

        while max_blocks > 0:
            if i + 1 == len(curr_config):
                i = -1
            i += 1
            val = curr_config[i]
            curr_config[i] = val + 1
            max_blocks += -1

        curr_config_s = ",".join([str(number) for number in curr_config])

    return len(configs)


def count_redistribution_cycles_two():
    # vars: count, len, configs, curr_config

    file = open('06.txt').read()
    banks = [int(number) for number in file.split(',')]

    configs = {}
    curr_config = banks
    curr_config_s = ",".join([str(number) for number in curr_config])

    while curr_config_s not in configs:
        configs[curr_config_s] = len(configs)
        max_blocks = max(curr_config)
        i = curr_config.index(max(curr_config))
        curr_config[i] = 0

        while max_blocks > 0:
            if i + 1 == len(curr_config):
                i = -1
            i += 1
            val = curr_config[i]
            curr_config[i] = val + 1
            max_blocks += -1

        curr_config_s = ",".join([str(number) for number in curr_config])

    return (len(configs) - configs[curr_config_s])
