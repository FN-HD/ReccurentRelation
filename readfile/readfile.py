def read_integerlist(filename='./readfile/primelist.txt'):
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

    Notes
    ----------
    If you write # in a line of file, then you comment out 
    this line. 
    '''
    integerlist = []
    
    with open(filename) as file:
        l = file.readlines()
        for p in l:
            if '#' not in p:
                integerlist.append(int(p))

    return integerlist

    