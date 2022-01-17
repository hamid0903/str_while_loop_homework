def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    punct=0
    while idx<len(s):
        if not s[idx].isalpha() and not s[idx].isdigit:
            punct+=1
        idx+=1
    return punct
print(main("20,**abc21"))