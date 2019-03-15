import random
import time
import tempfile


def bubble_sorter(iterable, reverse=False):
    if isinstance(iterable, list):
        iterable = iterable.copy()
    for i in range(len(iterable)):
        for j in range(i, len(iterable)):
            if reverse:
                if iterable[i] < iterable[j]:
                    iterable[i], iterable[j] = iterable[j], iterable[i]
            else:
                if iterable[i] > iterable[j]:
                    iterable[i], iterable[j] = iterable[j], iterable[i]
    return iterable


def qsorter(iterable, reverse=False):
    if len(iterable) < 2:
        return iterable
    r = random.choice(iterable)
    less = [i for i in iterable if i < r]
    equal = [i for i in iterable if i == r]
    greater = [i for i in iterable if i > r]
    if reverse:
        return qsorter(greater, reverse=True) + equal + qsorter(less, reverse=True)
    return qsorter(less) + equal + qsorter(greater)


def timer(func):
    def counter(*args):
        start = time.perf_counter()
        try:
            return func(*args)
        finally:
            print(time.perf_counter() - start)

    return counter


def logger(func):
    fl = open(r'C:\python\logs.txt', 'a')

    def writer(*args):
        try:
            return func(*args)
        finally:
            print(time.time(), str(func.__name__), sep='\t', file=fl)
            fl.close()

    return writer


def ranger(*args):
    # Analog of range() (xrange())
    assert 0 < len(args) < 4, '1-3 arguments expected, but %d given' % len(args)
    if len(args) == 1:
        start, step = 0, 1
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
        step = 1
    else:
        start, stop, step = args

    while start < stop:
        yield start
        start += step


class tmp_dir:
    # Context manager creating temporary folder.
    def __init__(self):
        self.directory = tempfile.mkdtemp()

    def __enter__(self):
        print('Directory created: ', self.directory)
        return self.directory

    def __exit__(self, exc_type, exc_value, exc_tb):
        shutil.rmtree(self.directory)
        if exc_type is None:
            print('Removed and exited')
        else:
            print('exception', exc_type)
