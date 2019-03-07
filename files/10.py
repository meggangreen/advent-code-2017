
def make_text_from_file(filepath):

    return open(filepath).read()


def make_lengths_from_text(text="3,4,1,5"):

    return [int(n) for n in text.split(',')]


def make_wheel(length):

    return list(range(length))
