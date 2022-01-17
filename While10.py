def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    numb=0
    while idx<len(s):
        if s[idx].isdigit():
            if int(s[idx])%2==1:
                numb+=int(s[idx])
        idx+=1
    return numb
print(main("12112112"))