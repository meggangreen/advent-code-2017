""" Analyze a list of passphrases; return the number of valid passphrases. """

def count_valid_passphrases_one():
    counter = 0

    with open('04.txt') as pp_file:
        for pp in pp_file:
            pp_word_list = pp.split()
            if len(set(pp_word_list)) == len(pp_word_list):
                counter += 1

    return counter


def count_valid_passphrases_two():
    """ My solution was going to count all of the letters. After having to write
        my own versions of built-in functions, I now forget that they even exist
        ... to the detriment of my code.

        The below solution is from madacoo:
        https://github.com/madacoo/advent_of_code_2017/blob/master/day04/solve.py

    """

    counter = 0
    with open('04.txt') as file:
        for pp in file:
            pp_word_list = [''.join(sorted(word)) for word in pp.split()]
            if len(set(pp_word_list)) == len(pp_word_list):
                counter += 1

            # counter += 1
            # word_list = passphrase.split()
            # if len(set(word_list)) != len(word_list):
            #     continue
            # word_dict = {word: {} for word in word_list}
            # for word in word_dict:
            #     for char in word:
            #         word_dict[word][char] = word_dict[word].get(char, 0) + 1
            # while word_list:
            #     # import pdb; pdb.set_trace()
            #     curr_word = word_list.pop()
            #     i = len(word_list)
            #     while i > 0:
            #         i -= 1
            #         is_anagram = True
            #         for char, count in word_dict[curr_word].items():
            #             if word_dict[word_list[i]].get(char, 0) >= count:
            #                 is_anagram = False
            #                 break
            #         if is_anagram is True:
            #             counter -= 1
            #             word_list = None
            #             break

    return counter


print "Num of valid passphrases"
print "Part 1: {}".format(count_valid_passphrases_one())
print "Part 2: {}".format(count_valid_passphrases_two())
