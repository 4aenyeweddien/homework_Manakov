# from datetime import datetime
from typing import Callable, Any
from functools import wraps


def log(filename: Any) -> Callable:
    """запись вызова функции и ее результат в файл или в консоль"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            result = func(*args, **kwargs)
            try:
                result == sum(args)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function ok\n")
                else:
                    print(f"my_function ok")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}. Inputs:{args}, {kwargs}\n")
                else:
                    print(f"my_function error: {e}. Inputs:{args}, {kwargs}")
            return result
        return wrapper
    return decorator


@log(filename="")
def my_function(x: int, y: int) -> int:
    """принимает два значения и складывает их"""
    return x + y


my_function("1", "2")
