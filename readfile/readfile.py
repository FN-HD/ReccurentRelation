def read_integerlist(filename):
    '''
    get a list of integers from a file
    
    Parameters
    ----------
    filename : str
        the name of the file
        
    Return
    ----------
    integerlist : list
        a list of integers written on the file

    '''
    integerlist = []
    
    with open(filename) as file:
        l = file.readlines()
        for p in l:
            integerlist.append(int(p))

    return integerlist

    