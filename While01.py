def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    numb=0
    while idx<len(s):
        if s[idx].isdigit():
            numb+=1
        idx+=1
    return numb
print(main("20abc21"))
