
def make_text_from_file(filepath):

    return open(filepath).read()


def make_lengths_from_text(text="3,4,1,5"):

    return [int(n) for n in text.split(',')]


class Wheel:
    def __init__(self, size):
        self.contents = list(range(size))
        self.start_i = 0

    def manipulate(self, length, skip):
        if length > len(self.contents):
            print("length invalid")
            return

        start = self.start_i

        # select sub
        if start + length >= len(self.contents):
            subself = self.contents[start:]
            subself += self.contents[:length-len(subself)]
        else:
            subself = self.contents[start:start+length]

        # reverse
        subself.reverse()

        # replace
        for i in range(len(subself)):
            if i + start >= len(self.contents):
                start = -i
            self.contents[i+start] = subself[i]

        # increment starting position
        self.start_i = (self.start_i + length + skip) % len(self.contents)


def part_one():
    wheel = Wheel(256)
    lengths = make_lengths_from_text(make_text_from_file('10.txt'))
    skip = 0

    for length in lengths:
        wheel.manipulate(length, skip)
        skip += 1

    return wheel.contents[0] * wheel.contents[1]


################################################################################
if __name__ == '__main__':
    print(f"Part 1: {part_one()}")
