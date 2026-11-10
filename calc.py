def mean(xs):
    """Arithmetic mean. Raises ValueError on an empty list."""
    if not xs:
        raise ValueError("Cannot compute mean of empty list")
    return sum(xs) / len(xs)


def median(xs):
    s = sorted(xs)
    n = len(s)
    if n % 2 == 0:
        return (s[n // 2 - 1] + s[n // 2]) / 2
    else:
        return s[n // 2]
