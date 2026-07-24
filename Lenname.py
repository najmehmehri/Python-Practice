"""
Decorators in Python

Problem: Create decorators that modify function behavior:
1. Check string length before printing
2. Check user permission before accessing admin page
Decorators wrap a function and add functionality before/after execution.
"""

from functools import wraps



# Decorator 1: String Length Checker


def check_string_length(max_length):
    """Decorator factory: checks if string length exceeds max_length"""
    def decorator(func):
        @wraps(func)
        def wrapper(name):
            if len(name) > max_length:
                print(f"Error: '{name}' is longer than {max_length} characters")
            else:
                func(name)
        return wrapper
    return decorator


@check_string_length(5)
def show_name(name):
    print(f"Name: {name}")



# Decorator 2: Permission Checker


def require_permission(has_permission):
    """Decorator factory: checks if user has permission"""
    def decorator(func):
        @wraps(func)
        def wrapper():
            if has_permission:
                func()
            else:
                print("Access denied: you don't have permission")
        return wrapper
    return decorator


@require_permission(True)
def go_to_admin_page():
    print("Welcome to admin page!")



# Test


if __name__ == "__main__":
    print("=" * 40)
    print("Testing String Length Decorator")
    print("=" * 40)
    show_name("ali")        # OK (3 chars)
    show_name("mohammad")   # Error (7 chars)
    
    print("\n" + "=" * 40)
    print("Testing Permission Decorator")
    print("=" * 40)
    go_to_admin_page()      # Has permission
    
    # Changing permission
    print("\n--- Without permission ---")
    no_permission = require_permission(False)(lambda: print("This won't run"))
    no_permission()