def clean_garbage(stream):
    stream = list(stream)

    g_alpha = "<"
    g_omega =">"

    garbage = []

    a, o = None, None
    for i, s in enumerate(stream):
        if s == g_alpha and not a:
            a = i
        if s == g_omega and a:
            o = find_garbage_end(stream[i-1:a:-1], i)
        if a and o:
            garbage.append(''.join(stream[a+1:o]))
            stream[a:o+1] = '_'*(o+1-a)
            a, o = None, None

    return ''.join(stream), garbage


def find_garbage_end(segment, i):
    if not segment:
        return i

    bangs = 0
    for s in segment:
        if s == '!':
            bangs += 1
        else:
            break

    return i if bangs % 2 == 0 else None


def calc_total_score(stream):
    total = 0
    group = 0
    for s in stream:
        if s == '{':
            group += 1
            total += group
        if s == '}':
            group += -1

    return total
