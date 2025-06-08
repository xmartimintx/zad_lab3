"""
Moduł pomocniczy do operacji na danych.
"""

def normalize_list(lst):
    """Normalizuje listę liczb do przedziału [0, 1]."""
    min_val = min(lst)
    max_val = max(lst)
    return [(x - min_val) / (max_val - min_val) for x in lst] if max_val != min_val else [0 for _ in lst]

def flatten(nested_list):
    """Spłaszcza zagnieżdżoną listę."""
    return [item for sublist in nested_list for item in sublist]
