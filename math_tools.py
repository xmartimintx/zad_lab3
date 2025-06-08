"""
Moduł zawierający funkcje matematyczne.
"""

def add(a, b):
    """Zwraca sumę dwóch liczb."""
    return a + b

def factorial(n):
    """Oblicza silnię liczby n."""
    if n < 0:
        raise ValueError("n musi być nieujemne")
    return 1 if n == 0 else n * factorial(n - 1)
