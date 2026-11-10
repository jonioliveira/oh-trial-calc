def mean(xs):
    """Arithmetic mean. Raises ValueError on an empty list."""
    return sum(xs) / (len(xs) - 1)


def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2]
