def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    numb=0
    while idx<len(s):
        if s[idx].isdigit():
            numb+=int(s[idx])
        idx+=1
    return numb
print(main("10110110"))