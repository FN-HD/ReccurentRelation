import pandas as pd

def get_conditional_table(condition_name, 
                          data_names, 
                          condition_list, 
                          data_lists):
    '''
    get a table of value of data_list with a condition
    
    Parameters
    ----------
    condition_name : str
        the name of first row in the table
    data_names : list
        the name of rows in the table
    condition_list : list
        the list of integers of first row
    data_lists : list
        the list of lists of data set
        
    Example
    ----------
    >>> primelist = [2, 3, 5, 7]
    >>> fib = [1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    >>> df = get_conditional_table('prime', 
                                    ['fib'], 
                                    primelist, 
                                    [fib])
    >>> print(df)
           0, 1, 2, 3
    prime  2, 3, 5, 7
    fib    1, 2, 5, 13

    Raises
    ----------
    TypeError
        If condition_name is not a str or data_names, 
        data_lists, or condition_lists are not a list.
    ValueError
        If data_names and data_lists have not same length

    '''
    if not isinstance(condition_name, str):
        raise TypeError('condition_name is not a str')
    if not isinstance(data_names, list):
        raise TypeError('data_names is not a list')
    if not isinstance(condition_list, list):
        raise TypeError('condition_lists is not a list')    
    if not isinstance(data_lists, list):
        raise TypeError('data_lists is not a list')
        
    if len(data_names) != len(data_lists):
        raise ValueError('data_lists and data_names have no same length.')
        
    table_lists = [[i for i in range(len(data_lists[0])) if i in condition_list]]
    
    for data_list in data_lists:
        if len(data_list) != len(data_lists[0]):
            raise ValueError(f'{data_list} is too short')
        table_lists.append([
            data_list[i] for i in table_lists[0]
                           ])
     
    pd.set_option('display.max_columns', len(table_lists[0]))
    
    index_names = [condition_name]
    index_names.extend(data_names)
    
    dataframe = pd.DataFrame(table_lists, 
                             index = index_names)
    
    return dataframe