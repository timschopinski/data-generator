import time
import inspect
import logging


logger = logging.getLogger(__name__)


def performance_measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Get module name
        module_name = inspect.getmodule(func).__name__

        logger.info(f"{module_name}.{func.__name__} took {elapsed_time:.4f} seconds to run.")
        return result
    return wrapper
