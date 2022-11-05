from datetime import datetime


def timer(func_name: str = "Function "):
    def decorate(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            end = datetime.now()
            time = end - start
            print(
                f"Function {func_name} execution time: {time.seconds}s, {time.microseconds} ms"
                )
            return result
        return wrapper
    return decorate