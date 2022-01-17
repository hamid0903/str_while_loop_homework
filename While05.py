def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    lower=0
    while idx<len(s):
        if s[idx].islower():
            lower+=1
        idx+=1
    return lower
print(main("20abcABCD21"))