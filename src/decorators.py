from datetime import datetime
from typing import Callable, Any
from functools import wraps


def log(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now().time()
            result = func(*args, **kwargs)
            end_time = datetime.now().time()
            try:
                result == sum(args)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Время начала работы функции: {start_time}\n")
                        file.write(f"my_function ok\nРезультат:{result}\n")
                        file.write(f"Время окончания работы функции: {end_time}\n")
                else:
                    print(f"Время начала работы функции:{start_time}")
                    print(f"my_function ok\nРезультат:{result}")
                    print(f"Время окончания работы функции:{end_time}")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}. Inputs:{args}, {kwargs}\n")
                else:
                    print(f"my_function error: {e}. Inputs:{args}, {kwargs}")
            return result
        return wrapper
    return decorator


@log(filename="src/mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
