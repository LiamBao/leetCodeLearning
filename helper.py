import time
import functools

def timeit(func):
    """
    logging function execute duration.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_timestamp = time.time()
        result = func(*args, **kwargs)
        print('time cost {duration}'.format(duration=time.time() - start_timestamp))
        return result

    return wrapper