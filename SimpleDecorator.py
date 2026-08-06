"""
Simple Decorator
"""

from functools import wraps


def log_function_name(func):
    """
    Decorator that prints the function name before calling it
    """
    @wraps(func)  # Preserves func's metadata (name, docstring, etc.)
    def wrapper(*args, **kwargs):
        print(f"▶ Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"◀ Finished: {func.__name__}")
        return result
    return wrapper


@log_function_name
def say_hello(name, family):
    """Says hello to a person"""
    print(f"Hello {name} {family}")


@log_function_name
def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    # Test the decorated functions
    say_hello("mohammad", "ordookhani")
    
    print("\n" + "-" * 30)
    
    result = add_numbers(5, 3)
    print(f"Result: {result}")
    
    print("\n" + "-" * 30)
    print(f"Function name: {say_hello.__name__}")
    print(f"Docstring: {say_hello.__doc__}")