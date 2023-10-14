from functools import wraps
from datetime import datetime


def time_counter(f):

    @wraps(f)
    def return_func(*args, **kwargs):
        start = datetime.now()
        res = f(*args, **kwargs)
        end = datetime.now()
        diff = end - start
        print(f'Time passed - {diff.seconds}.{diff.microseconds} s')
        return res

    return return_func
