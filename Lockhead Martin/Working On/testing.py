import math

def round_half_up(n, decimals=0):
    """
    Rounds n to the specified number of decimals.
    .5 values always round up. For example:
      2.5 -> 3, 3.5 -> 4, and -2.5 -> -2.
    """
    factor = 10 ** decimals
    return math.floor(n * factor + 0.5) / factor

# Examples:
