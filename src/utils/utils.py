from random import randrange
from time import gmtime, process_time, strftime


def randstr(charlist, length):
    """Generates a string with characters chosen at random from the string
    received as first argument. If an empty string is received, lower
    and upper case letters and decimal digits are used by default.

    Positional arguments:
    charlist -- Characters than can appear in the result.
    length -- Desidred length of the resulting string.
    """
    res = ""
    chars = ""
    if not charlist:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    else:
        chars = charlist
    l = len(chars)

    for _ in range(length):
        nextchar = randrange(l)
        res = res + chars[nextchar]
    return res


def show_process_time(original_function):
    """Decorator that prints the process time elapsed during the execution
    of the function decorated, up to seconds precision.
    https://docs.python.org/dev/library/time.html#time.process_time
    """

    def timed_function(*args, **kwargs):
        start = process_time()
        res = original_function(*args, **kwargs)
        end = process_time()
        print(strftime("CPU time elapsed: %H:%M:%S", gmtime(end - start)))
        return res

    return timed_function


def subsequences(sequence):
    """Returns a generator of all the sub-sequences of target sequence,
    that preserve the order of the elements. Each sub-sequence is represented
    as a tuple.

    Example:

    for i, e in enumerate(subsequences([1, 2])):
        print(i, e)

    --> 0 ()
    --> 1 (1,)
    --> 2 (1, 2)
    --> 3 (2,)
    """
    elems = len(sequence)
    yield ()
    for startidx in range(elems):
        for endidx in range(startidx, elems):
            subsequence = tuple(sequence[startidx : endidx + 1])
            yield subsequence
