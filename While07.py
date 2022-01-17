def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    numb=0
    while idx<len(s):
        if s[idx].isdigit():
            if int(s[idx])%2==0 and int(s[idx])!=0:
                numb+=1
            else:
                numb+=0
        idx+=1
    return numb
print(main("20abc21"))