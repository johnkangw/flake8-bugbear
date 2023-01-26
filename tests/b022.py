"""
Should emit:
B022 - on lines 8
"""


import contextlib

with contextlib.suppress():
    raise ValueError

with contextlib.suppress(ValueError):
    raise ValueError

exceptions_to_suppress = [ValueError]
with contextlib.suppress(*exceptions_to_suppress):
    raise ValueError
