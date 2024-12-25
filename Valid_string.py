def announce_result(val):
    """
    Given string as input must start with small character and end with the capital letter such as..
    valid : 'aA', 'aAbB', 'aAcCdD'
    invalid : 'aa', 'Bb', 'ab', 'cd'
    """
    if len(val) % 2 == 0:
        for i in range(0,len(val)-1,2):
            if (ord(val[i]) - 32) != ord(val[i+1]):
                return False
        else:
            return True
    else:
        return False
                
announce_result("aAbB")
