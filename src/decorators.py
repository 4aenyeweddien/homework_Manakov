# from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """запись вызова функции и ее результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # result = func(*args, **kwargs)
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("my_function ok\n")
                    return result
                else:
                    print("my_function ok")
                    return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}. Inputs:{args}, {kwargs}\n")
                else:
                    print(f"my_function error: {e}. Inputs:{args}, {kwargs}")

        return wrapper
    return decorator


@log()
def my_function(x: int, y: int) -> int:
    """принимает два значения и складывает их"""
    return x + y


my_function(1, 2)
