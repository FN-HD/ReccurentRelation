import pandas as pd

def get_conditional_table(condition_name, 
                          data_name, 
                          condition_list, 
                          data_list):
    '''
    get a table of value of data_list with a condition
    
    Parameters
    ----------
    condition_name : str
        the name of first row in the table
    data_name : str
        the name of second row in the table
    condition_list : list
        the list of integers of first row
    data_list : list
        the list of data set
        
    Example
    ----------
    >>> primelist = [2, 3, 5, 7]
    >>> fib = [1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    >>> df = get_conditional_table('prime', 
                                    'fib', 
                                    primelist, 
                                    fib)
    >>> print(df)
            0, 1, 2, 3
    *******************
    prime | 2, 3, 5, 7
    fib   | 1, 2, 5, 13

    Raises
    ----------
    TypeError
        If condition is not a str or data_name is not a str.


    '''
    if not isinstance(condition_name, str):
        raise TypeError('rowname1 is not a str')
        
    if not isinstance(data_name, str):
        raise TypeError('rowname2 is not a str')
    
    lists = [[], []]
    
    for i, values in enumerate(data_list):
        if i in condition_list:
            lists[0].append(i)
            lists[1].append(values)
     
    pd.set_option('display.max_columns', len(lists[0]))
    
    dataframe = pd.DataFrame(lists, 
                             index=[condition_name, data_name])
    
    return dataframe