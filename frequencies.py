from collections import Counter

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
	items = [str(x) for x in items]
	return dict(Counter(items))
