def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    s=s.lower()
    idx = 0
    cons = 0
    while idx < len(s):
        if s[idx].isalpha():
            if s[idx]!="a" or s[idx]!="e" or s[idx]!="i" or s[idx]!="o" or s[idx]!="u":
                cons+=1
        idx += 1
    return cons
print(main("abcdefghklmnopqrstUVWXYZ"))