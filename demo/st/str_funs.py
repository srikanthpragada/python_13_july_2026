def has_space(s: str) -> bool:
    return s.find(' ') >= 0

def has_upper(s: str) -> bool:
    for c in s:
        if c.isupper():
            return True

    return False