def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    upper=0
    while idx<len(s):
        if s[idx].isupper():
            upper+=1
        idx+=1
    return upper
print(main("20abcABCD21"))