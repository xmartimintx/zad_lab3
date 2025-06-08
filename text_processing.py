"""
Moduł do przetwarzania tekstu.
"""

def word_count(text):
    """Zlicza liczbę słów w tekście."""
    return len(text.split())

def is_palindrome(s):
    """Sprawdza, czy tekst jest palindromem."""
    s_clean = ''.join(c.lower() for c in s if c.isalnum())
    return s_clean == s_clean[::-1]
