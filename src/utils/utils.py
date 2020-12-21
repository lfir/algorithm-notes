from random import randrange
from time import gmtime, process_time, strftime

 
def printNumTable(table):
    """Prints the received table (2D array) with column and row numbers 
    and fixed column width (1 tab, up to 7 characters per cell).
    """
    header = [''] + ['c' + str(x) for x in range(len(table[0]))]
    print('\t'.join([elem for elem in header]))
    print('\n'.join(['\t'.join(['r' + str(i)] + [str(cell) for cell in row]) for i, row in enumerate(table)]))

def randstr(charlist, length):
    """Generates a string with characters chosen at random from the string
    received as first argument. If an empty string is received, lower
    and upper case letters and decimal digits are used by default.
    :param charlist: str Characters than can appear in the result.
    :param length: int Length of the resulting string.
    :return: str Randomly generated string.
    """
    res = ''
    chars = ''
    if not charlist:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
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
    :param original_function: callable Function to be timed.
    :return: callable Decorated function.
    """
    def timed_function(*args, **kwargs):
        start = process_time()
        res = original_function(*args, **kwargs)
        end = process_time()
        print(strftime('CPU time elapsed: %H:%M:%S', gmtime(end - start)))
        return res
    return timed_function

def subsequences(sequence):
    """Returns one a time all the sub-sequences of target sequence,
    that preserve the order of the elements.
    Example:
    for i, e in enumerate(subsequences([1, 2])):
        print(i, e)                        
  
    --> 0 ()
    --> 1 (1,)
    --> 2 (1, 2)
    --> 3 (2,)
    :param sequence: sequence Target sequence.
    :return: generator All the subsequences.
    """
    elems = len(sequence)
    yield ()
    for startidx in range(elems):
        for endidx in range(startidx, elems):
            subsequence = tuple(sequence[startidx:endidx+1])
            yield subsequence
